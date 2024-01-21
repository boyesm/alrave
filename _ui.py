from tkinter import *


def initializeUi(self):
    window = Tk()
    window.configure(bg="lightblue")

    window.columnconfigure(0, weight=1)
    window.columnconfigure(3, weight=1)
    window.columnconfigure(6, weight=1)
    window.rowconfigure(4, weight=1)

    window.title("AlexRave - The Sound of The Future")
    window.geometry('1000x600')

    title = Label(window, text="AlRave", font=("Helvetica", 24))
    title.grid(sticky="nsew", column=0, row=0, columnspan=9, padx=10, pady=10)

    label = Label(window, text="Enter a BPM")
    label.grid(sticky="nsew", column=0, row=1, columnspan=2)

    bpm_spin_value = StringVar()
    bpm_spin_value.set("60")

    bpm_spin = Spinbox(window, from_=60, to=180, textvariable=bpm_spin_value)
    bpm_spin.grid(sticky="nsew", column=2, row=1, columnspan=3)

    # Create text box for pause and play, drum code, bass code, melody code

    # Pause and play boxes

    button_play = Button(window, text="Play", command=self.play)
    button_play.grid(sticky="nsew", column=5, row=1, columnspan=2)

    button_pause = Button(window, text="Pause II", command=self.pause)
    button_pause.grid(sticky="nsew", column=7, row=1, columnspan=2)

    def updateKickCode(code):
        kick_update_message = self.kick.updateSoundGenerationFunction(code)
        # update kick message

    def updateBassCode(code):
        bass_update_message = self.bass.updateSoundGenerationFunction(code)
        # update bass message

    def updateMelodyCode(code):
        melody_update_message = self.melody.updateSoundGenerationFunction(code)
        # update melody message

    # Drum code input box
    drum_code = Text(window, width=25, height=9)
    drum_code.insert(END, self.default_drum_code)
    drum_code.grid(sticky="nsew", column=0, row=4, columnspan=3, padx=10, pady=10)

    drum_code_label = Label(window, text="Drum code here:")
    drum_code_label.grid(sticky="nsew", column=0, row=3, columnspan=3, padx=10, pady=10)

    drum_code_button = Button(
        window,
        text="Update Code",
        command=lambda: updateKickCode(drum_code.get("1.0", "end")))
    drum_code_button.grid(sticky="nsew", column=0, row=5, columnspan=3, padx=10, pady=10)

    # Bass code input box
    bass_code = Text(window, width=25, height=9)
    bass_code.insert(END, self.default_bass_code)
    bass_code.grid(sticky="nsew", column=3, row=4, columnspan=3, padx=10, pady=10)

    bass_code_label = Label(window, text="Bassline code here:")
    bass_code_label.grid(sticky="nsew", column=3, row=3, columnspan=3, padx=10, pady=10)

    bass_code_button = Button(window,
                              text="Update Code",
                              command=lambda: updateBassCode(bass_code.get("1.0", "end")))

    bass_code_button.grid(sticky="nsew", column=3, row=5, padx=10, pady=10)

    # Melody code input box
    melody_code = Text(window, width=25, height=9)
    melody_code.insert(END, self.default_melody_code)
    melody_code.grid(sticky="nsew", column=6, row=4, columnspan=3, padx=10, pady=10)

    melody_code_label = Label(window, text="Melody code here:")
    melody_code_label.grid(sticky="nsew", column=6, row=3, columnspan=3, padx=10, pady=10)

    melody_code_button = Button(window,
                                text="Update Code",
                                command=lambda: updateMelodyCode(melody_code.get("1.0", "end")))  # Enter command

    melody_code_button.grid(sticky="nsew", column=6, columnspan=3, row=5, padx=10, pady=10)

    return window
