from scipy.signal import butter, sosfiltfilt

def bandpass_filter(signal, low, high, fs):
    sos = butter(
        4,
        [low, high],
        btype='bandpass',
        fs=fs,
        output='sos'
    )
    return sosfiltfilt(sos, signal)

filtered_ecg = bandpass_filter(
    ecg_signal, 0.5, 40, sampling_rate
)