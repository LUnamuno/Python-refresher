import numpy as np
import pytest

from signal_denoiser import (
    amplitude_spectrum,
    butter_lowpass,
    dominant_frequency,
    lowpass_fft,
    make_noisy_image,
    make_noisy_signal,
    notch_fft,
    remove_periodic_noise,
    rmse,
    snr_db,
)

FS = 500


@pytest.fixture(scope="module")
def sig():
    return make_noisy_signal(duration=2.0, fs=FS)


def test_provided_generators():                         # must pass from the start
    t, clean, noisy = make_noisy_signal()
    assert t.shape == clean.shape == noisy.shape == (1000,)
    clean_img, noisy_img = make_noisy_image()
    assert clean_img.shape == noisy_img.shape == (128, 128)
    assert rmse(clean_img, noisy_img) > 0.3


def test_amplitude_spectrum_of_pure_sine():
    t = np.arange(0, 1, 1 / FS)
    freqs, amp = amplitude_spectrum(0.7 * np.sin(2 * np.pi * 25 * t) + 2.0, FS)
    assert freqs[0] == 0 and freqs[-1] == pytest.approx(FS / 2)
    assert len(freqs) == len(amp) == FS // 2 + 1
    assert amp[25] == pytest.approx(0.7, abs=1e-9)
    assert amp[0] == pytest.approx(2.0, abs=1e-9)           # DC component is not doubled
    assert np.argmax(amp[1:]) + 1 == 25


def test_dominant_frequency(sig):
    t, clean, noisy = sig
    assert dominant_frequency(clean, FS) == pytest.approx(5.0)
    assert dominant_frequency(noisy, FS) == pytest.approx(5.0)       # the 60 Hz hum is weaker than the signal
    assert dominant_frequency(clean + 10, FS) == pytest.approx(5.0)  # DC is ignored
    assert dominant_frequency(np.sin(2 * np.pi * 60 * t), FS) == pytest.approx(60.0)


def test_lowpass_removes_the_hum(sig):
    _, clean, noisy = sig
    out = lowpass_fft(noisy, FS, cutoff=20)
    assert out.shape == noisy.shape and np.isrealobj(out)
    assert rmse(out, clean) < 0.25 * rmse(noisy, clean)
    assert dominant_frequency(out, FS) == pytest.approx(5.0)


def test_lowpass_with_huge_cutoff_is_identity(sig):
    _, _, noisy = sig
    assert np.allclose(lowpass_fft(noisy, FS, cutoff=1e6), noisy)


def test_notch_removes_only_the_hum(sig):
    _, clean, noisy = sig
    out = notch_fft(noisy, FS, f0=60, width=2)
    freqs, amp = amplitude_spectrum(out, FS)
    assert amp[np.abs(freqs - 60) <= 2].max() < 1e-9
    assert amp[np.abs(freqs - 5) < 0.6].max() > 0.9                  # the 5 Hz tone survives
    assert rmse(out, clean) < rmse(noisy, clean)


def test_butterworth_lowpass(sig):
    _, clean, noisy = sig
    out = butter_lowpass(noisy, FS, cutoff=20, order=4)
    assert out.shape == noisy.shape
    assert rmse(out, clean) < 0.4 * rmse(noisy, clean)


def test_rmse_and_snr():
    a = np.array([1.0, 2.0, 3.0])
    assert rmse(a, a) == 0.0
    assert rmse(a, a + 2) == pytest.approx(2.0)
    assert snr_db(a, a) == float("inf")
    assert snr_db(a, a * 1.1) == pytest.approx(20.0, abs=1e-9)       # error = 10 % of the signal -> 20 dB
    assert snr_db(a, 0 * a) == pytest.approx(0.0)


def test_snr_improves_after_filtering(sig):
    _, clean, noisy = sig
    assert snr_db(clean, lowpass_fft(noisy, FS, 20)) > snr_db(clean, noisy) + 10


def test_remove_periodic_noise_from_image():
    clean, noisy = make_noisy_image(size=128, freq=20, amp=0.5)
    restored = remove_periodic_noise(noisy)
    assert restored.shape == noisy.shape and np.isrealobj(restored)
    assert rmse(restored, clean) < 0.2 * rmse(noisy, clean)


def test_remove_periodic_noise_keeps_a_clean_image():
    clean, _ = make_noisy_image(size=128)
    assert rmse(remove_periodic_noise(clean), clean) < 0.01


def test_remove_periodic_noise_other_frequency():
    clean, noisy = make_noisy_image(size=96, freq=13, amp=0.8, seed=3)
    assert rmse(remove_periodic_noise(noisy), clean) < 0.2 * rmse(noisy, clean)
