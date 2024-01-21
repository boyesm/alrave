import time
from audio import Instrument

class Main:
    beat_number = 0
    is_playing = False

    interval = 0.5

    window = 0

    default_drum_code = """import numpy as np
duration=0.2
frequency=100.0
sampling_rate=44100

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the waveform (in this case, a simple sine wave)
audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)"""

    default_bass_code = """# use the variable `beat_number` to access the beat number. this value loops from 0 -> 7. use this to change the note based on time.
import numpy as np
duration=0.2
frequency=100.0
sampling_rate=44100

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the waveform (in this case, a simple sine wave)
audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
"""

    default_melody_code = """import numpy as np
sample_rate = 44100
duration = 5
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_data = 0.5 * np.sin(2 * np.pi * 440 * t)
"""

    kick = Instrument(default_drum_code)
    bass = Instrument(default_bass_code)
    melody = Instrument(default_melody_code)

    from _ui import initializeUi

    def pause(self):
        self.is_playing = False
        print("paused")

    def play(self):
        self.is_playing = True
        print("playing")

    def incrementBeatNumber(self):
        # 8 beats per loop, 0 -> 7
        if (self.beat_number >= 7):
            self.beat_number = 0
        else:
            self.beat_number += 1

    def run(self):

        window = self.initializeUi()

        while True:
            start_time = time.time()

            if (self.is_playing):
                # self.kick.playNextStep(self.beat_number)
                self.bass.playNextStep(self.beat_number)
                # self.melody.playNextStep(self.beat_number)
                self.incrementBeatNumber()

            window.update_idletasks()
            window.update()


            if (self.is_playing):
                elapsed_time = time.time() - start_time
                time.sleep(max(0, self.interval - elapsed_time))  # make timing much more precise here



if (__name__ == "__main__"):
    main = Main()
    main.run()