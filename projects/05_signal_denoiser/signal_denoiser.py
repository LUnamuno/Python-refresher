"""Project 05 - Signal denoiser: use the Fourier transform to remove periodic noise from 1-D signals and images.

Fill in every function marked ``raise NotImplementedError`` and run::

    python -m pytest projects/05_signal_denoiser -q
"""
from __future__ import annotations
import numpy as np
from scipy import fft, signal

def make_noisy_signal(duration: float=2.0, fs: int=500, signal_hz: float=5.0, hum_hz: float=60.0, hum_amp: float=0.8, noise_std: float=0.2, seed: int=0) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """PROVIDED. Returns ``(t, clean, noisy)``: a sine of ``signal_hz``, plus a mains-hum sine of ``hum_hz`` and white noise."""
    t = np.arange(0, duration, 1 / fs)
    clean = np.sin(2 * np.pi * signal_hz * t)
    rng = np.random.default_rng(seed)
    noisy = clean + hum_amp * np.sin(2 * np.pi * hum_hz * t) + noise_std * rng.normal(size=t.size)
    return (t, clean, noisy)

def make_noisy_image(size: int=128, freq: int=20, amp: float=0.5, seed: int=0) -> tuple[np.ndarray, np.ndarray]:
    """PROVIDED. Returns ``(clean, noisy)``: a smooth 2-D Gaussian blob and the same image plus a periodic stripe pattern
    (``amp * sin(2 pi * freq * x / size)``, i.e. vertical stripes) and a little white noise."""
    y, x = np.mgrid[0:size, 0:size] / size
    clean = np.exp(-((x - 0.5) ** 2 + (y - 0.5) ** 2) / 0.05)
    rng = np.random.default_rng(seed)
    noisy = clean + amp * np.sin(2 * np.pi * freq * x) + 0.02 * rng.normal(size=clean.shape)
    return (clean, noisy)

def amplitude_spectrum(x: np.ndarray, fs: float) -> tuple[np.ndarray, np.ndarray]:
    """One-sided amplitude spectrum of a real signal: ``(freqs, amplitude)`` with ``freqs`` in Hz from ``0`` to ``fs / 2``
    (``scipy.fft.rfftfreq``) and ``amplitude = |rfft(x)| / len(x)``, multiplied by 2 except for the DC and (if present)
    Nyquist bins, so that a unit-amplitude sine shows a peak of height ~1."""
    raise NotImplementedError

def dominant_frequency(x: np.ndarray, fs: float) -> float:
    """Frequency (Hz) of the highest peak of the amplitude spectrum, ignoring the DC component (0 Hz)."""
    raise NotImplementedError

def lowpass_fft(x: np.ndarray, fs: float, cutoff: float) -> np.ndarray:
    """Zero every Fourier coefficient above ``cutoff`` Hz and transform back (``rfft`` / ``irfft``, same length as ``x``)."""
    raise NotImplementedError

def notch_fft(x: np.ndarray, fs: float, f0: float, width: float=2.0) -> np.ndarray:
    """Remove the band ``f0 - width <= f <= f0 + width`` (Hz) of the spectrum and return the filtered signal (same length)."""
    raise NotImplementedError

def butter_lowpass(x: np.ndarray, fs: float, cutoff: float, order: int=4) -> np.ndarray:
    """Zero-phase Butterworth low-pass filter: ``scipy.signal.butter(order, cutoff, fs=fs)`` + ``scipy.signal.filtfilt``."""
    raise NotImplementedError

def rmse(a: np.ndarray, b: np.ndarray) -> float:
    """Root mean squared error between two arrays of the same shape."""
    raise NotImplementedError

def snr_db(clean: np.ndarray, estimate: np.ndarray) -> float:
    """Signal-to-noise ratio in decibels: ``10 * log10(sum(clean**2) / sum((estimate - clean)**2))``.
    A perfect estimate gives ``inf``."""
    raise NotImplementedError

def remove_periodic_noise(img: np.ndarray, center_radius: int=8, threshold: float=8.0) -> np.ndarray:
    """Remove periodic (stripe-like) noise from a grey image.

    1. ``F = fftshift(fft2(img))``; ``mag = |F|``.
    2. A coefficient is *suspicious* if it lies farther than ``center_radius`` pixels from the centre of the shifted
       spectrum (the low frequencies describe the picture itself and must be kept) **and** its magnitude exceeds
       ``threshold`` times the median magnitude of all coefficients outside that radius.
    3. Set the suspicious coefficients to 0, ``ifftshift`` + ``ifft2`` back and return the real part (same shape as ``img``).
    """
    raise NotImplementedError
