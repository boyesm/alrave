import numpy as np
import sounddevice as sd

class Instrument:
    audio_code: str = ""

    def __init__(self, audio_code):
        print("init instrument")
        self.audio_code = audio_code

    # this returns a string that is displayed to the user when they try to update the sound gen func
    def updateSoundGenerationFunction(self, code):
        # verify this code is valid by running it and putting into a numpy array
        print(code)
        try:
            beat_number = 0
            exec_globals = {'beat_number': beat_number}
            exec(code, exec_globals)
            audio_data = exec_globals["audio_data"]
            if (type(audio_data) != np.ndarray):
                raise ValueError("Output type is not a Numpy array.")
            self.audio_code = code
            print("Successfully updated.")
            return "Updated."
        except Exception as e:
            print(f"Failed to update due to: {e}")
            return f"Failed to update due to: {e}"

    def playNextStep(self, beat_number):
        # this is a numpy array
        exec_globals = {'beat_number': beat_number}
        exec(self.audio_code, exec_globals)  # how can I pass this code the beat number?
        audio_data = exec_globals["audio_data"]
        # play(audio_data)   # this is pseudo code!
        # print(audio_data)
        sd.play(audio_data / 3, 44100)
        # print(f"bmpsz {beat_number}")

