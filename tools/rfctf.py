"""Optional helpers for the RF Analysis Track.

Import it:

    import sys; sys.path.insert(0, "tools")
    from rfctf import load_sigmf, tune, lowpass, fm_demod, save_wav

or run it for a quick look at any SigMF recording:

    python3 tools/rfctf.py challenges/01-dots-and-dashes/keyed_carrier
"""
import json
import sys
import wave

import numpy as np


def load_sigmf(base):
    """Load `base`.sigmf-meta / `base`.sigmf-data. Returns (complex samples, sample rate)."""
    base = base.replace('.sigmf-meta', '').replace('.sigmf-data', '')
    meta = json.load(open(base + '.sigmf-meta'))
    raw = np.fromfile(base + '.sigmf-data', dtype='<i2').astype(np.float64)
    return raw[0::2] + 1j * raw[1::2], meta['global']['core:sample_rate']


def tune(iq, f0, fs):
    """Move the signal at offset f0 (Hz) to the centre of the recording."""
    return iq * np.exp(-2j * np.pi * f0 * np.arange(len(iq)) / fs)


def lowpass(x, cutoff, fs, ntaps=257):
    """Windowed-sinc low-pass filter. Output is time-aligned with the input."""
    n = np.arange(ntaps) - (ntaps - 1) / 2
    h = np.sinc(2 * cutoff / fs * n) * np.blackman(ntaps)
    return np.convolve(x, h / h.sum(), mode='same')


def fm_demod(iq, fs):
    """Instantaneous frequency in Hz (one sample shorter than the input)."""
    return np.angle(iq[1:] * np.conj(iq[:-1])) * fs / (2 * np.pi)


def save_wav(path, audio, fs):
    """Save a real signal as 16-bit mono WAV, scaled to its own peak, for listening."""
    a = np.asarray(audio, dtype=np.float64)
    a = a / (np.max(np.abs(a)) or 1.0)
    with wave.open(path, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(int(fs))
        w.writeframes((a * 32000).astype('<i2').tobytes())


def quicklook(base):
    iq, fs = load_sigmf(base)
    amp = np.abs(iq)
    print(f'samples      : {len(iq)}')
    print(f'sample rate  : {fs} Hz  (shows {-fs / 2:.0f} .. {fs / 2:.0f} Hz)')
    print(f'duration     : {len(iq) / fs:.2f} s')
    print(f'amplitude    : median {np.median(amp):.0f}, max {amp.max():.0f}')
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print('matplotlib not installed: skipping the spectrogram')
        return
    fig, ax = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
    step = max(1, len(iq) // 20000)
    ax[0].plot(np.arange(len(iq))[::step] / fs, amp[::step], lw=0.5)
    ax[0].set_ylabel('amplitude')
    ax[1].specgram(iq, NFFT=1024, Fs=fs, noverlap=512)
    ax[1].set_ylabel('frequency offset (Hz)')
    ax[1].set_xlabel('time (s)')
    out = base.replace('.sigmf-meta', '').replace('.sigmf-data', '') + '_quicklook.png'
    fig.savefig(out, dpi=110, bbox_inches='tight')
    print(f'spectrogram  : {out}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    quicklook(sys.argv[1])
