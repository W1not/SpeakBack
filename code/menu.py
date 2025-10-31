import tkinter as tk
import speechinput as si

class GUI:
    def speech_start():
        si.speechDetector.speech_usage(1)

    def visual():
        root = tk.Tk()
        root.title("Speech")
        root.geometry("400x300")
        label = tk.Label(root, text="Say exit to finish recognition")
        label.pack()

        label2 = tk.Label(root, text="Press Start to begin")
        label2.pack()


        start_speech_button = tk.Button(root, text="Start", command=GUI.speech_start)
        start_speech_button.pack()
        root.mainloop()