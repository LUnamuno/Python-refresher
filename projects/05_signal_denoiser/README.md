# Project 05 - Signal denoiser (FFT, SciPy)

Remove mains hum from a 1-D signal and periodic stripes from an image using the Fourier transform.

**Skills:** NumPy arrays and masks, `scipy.fft`, `scipy.signal` (Butterworth + `filtfilt`), 2-D FFT, evaluation metrics (RMSE, SNR in dB), matplotlib.
**Notebooks to review first:** 06 (NumPy), 07 (matplotlib), 09 (SciPy and SymPy).

## How to work

1. Open `signal_denoiser.py`; the two data generators are provided.
2. `python -m pytest projects/05_signal_denoiser -q` (skipped = not implemented yet).

## Milestones

1. Inspect - `amplitude_spectrum`, `dominant_frequency`.
2. 1-D filters - `lowpass_fft`, `notch_fft`, `butter_lowpass`.
3. Metrics - `rmse`, `snr_db`.
4. 2-D - `remove_periodic_noise` (find the spikes in the shifted 2-D spectrum and zero them).

## Stretch goals

- Plot signal, spectrum and filtered result in a 3x1 figure (`plt.subplots`); do the same for the image and its 2-D spectrum (`np.log1p(abs(F))`).
- Compare your FFT low-pass with the Butterworth filter near the cutoff (ringing vs smooth roll-off).
- Try `scipy.signal.spectrogram` on a chirp.
- Remove the noise automatically: detect the hum frequency with `dominant_frequency` on the residual instead of passing `f0`.
