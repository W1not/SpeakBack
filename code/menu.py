import tkinter as tk
import threading
import speechinput as si

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speech")
        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Say 'exit' to finish recognition")
        self.label.pack(pady=10)

        self.start_speech_button = tk.Button(self.root, text="Start", command=self.speech_start)
        self.start_speech_button.pack(pady=10)

    def speech_start(self):
        """Hilo separado de reconocimiento"""
        tts_program = threading.Thread(target=si.speechDetector.speech_usage, args=(1,))
        tts_program.daemon = True
        tts_program.start()
        self.label.config(text="Speech recognition started...")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GUI()
    app.run()
