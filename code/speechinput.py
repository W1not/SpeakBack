import speech_recognition as sr
import pyaudio
import pyttsx3


class speechDetector:
    # Init tts
    def __init__(self, input_device_index=0, language= "es-MX"):
        self.recognizer = sr.Recognizer()
        self.input_device_index = input_device_index
        self.language = language

    #Make a list of input devices
    def list_input_devices(self):
        p = pyaudio.PyAudio()
        print("---Dispositivos de entrada---")
        for i in range(p.get_device_count()):
            list_device = p.get_device_info_by_index(i)
            if list_device["maxInputChannels"] >= 1:
                print("Microfono ",  list_device["index"] , " " , list_device["name"])
        p.terminate()

    
    def text_to_speech(self,text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def listen_and_recognize(self):
        with sr.Microphone(device_index=self.input_device_index) as source:
            print("Escuchando... di algo: ")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio,language=self.language)
            print(text)
            return text
        except sr.UnknownValueError:
            print("No se entendió el audio.")
        except sr.RequestError as e:
            print("Error al conectar con el servicio:", e)
        return None
    
    def run(self):
        while True:
            text = self.listen_and_recognize()
            if not text:
                continue
            self.text_to_speech(text)
            if "salir" in text.lower() or "exit" in text.lower():
                print("saliendo")
                break

