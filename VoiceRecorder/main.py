# Import sounddevice package
import sounddevice as sd
# sounddevice package is used for voice recording and playing

# Import numpy package. The sounddevice package uses numpy package for voice processing and sampling
import numpy as np

# Import soundfile package
import soundfile as sf
# soundfile package is used for reading and writing voice files.

# Import time package. For keeping time values
from time import time

# For elapsed time knowledge, we need to define a start time
start_time = time()

def recording(duration, file_name):
    fs = 44100
    # Sample rate

    record_count = int(duration * fs)

    record = sd.rec(frames=record_count, samplerate=fs, channels=2)
    # channels = 2 means stereo
    sd.wait()
    # Waiting for the end of the recording

    sf.write(file_name, record, fs)
    # Save the voice file

# Defining record duration by asking the user
duration = int(input("Enter the duration as the seconds' type, please: "))

# Defining a file name by asking the user
file_name = input("Enter a name for recording file please (i.e. record.wav): ")

# Call the record function to the recording process
recording(duration, file_name)

# For elapsed time knowledge, we need to define an end time
end_time = time()

# Calculating the elapsed time
elapsed_time = end_time - start_time

# Giving information about recording and writing time
print("\nRecording completed in {:.2f} seconds.".format(elapsed_time))
