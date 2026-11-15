import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt


# Load ECG recording locally
record = wfdb.rdrecord('mitdb/101')

# Extract ECG signal (first channel)
ecg_signal = record.p_signal[:, 0]

# Get sampling frequency
sampling_rate = record.fs

print("Sampling Rate:", sampling_rate)
print("Number of samples:", len(ecg_signal))



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
    ecg_signal,
    0.5,
    40,
    sampling_rate
)

print("Filtering completed!")

# time = np.arange(len(ecg_signal)) / sampling_rate

# plt.figure(figsize=(12, 5))

# plt.plot(time[:1800], ecg_signal[:1800],
#          label="Original ECG")

# plt.plot(time[:1800], filtered_ecg[:1800],
#          label="Filtered ECG")

# plt.xlabel("Time (seconds)")
# plt.ylabel("Amplitude (mV)")
# plt.legend()
# plt.grid()
# plt.show()


# Number of samples
N = len(filtered_ecg)

# Apply FFT
fft_values = np.fft.rfft(filtered_ecg)

# Calculate corresponding frequencies
frequencies = np.fft.rfftfreq(
    N,
    d=1/sampling_rate
)

# Calculate magnitude
magnitude = np.abs(fft_values)

# Plot frequency spectrum
plt.figure(figsize=(12, 5))

plt.plot(frequencies, magnitude)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("ECG Frequency Spectrum")

plt.xlim(0, 60)
plt.grid()

plt.show()