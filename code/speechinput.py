import speech_recognition as sr
import pyttsx3
import pyaudio
import os


class speechDetector:
    #Make a list of input devices
    def speech_search():
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            list_device = p.get_device_info_by_index(i)
            if list_device["maxInputChannels"] >= 1:
                print("Microfono ",  list_device["index"] , " " , list_device["name"])

    def speech_configurator(index,output):
        print(index)
        print(output)

    def speech_usage(input_device):
        queue_speech = []
        #Inicializador de speech_recognition
        r = sr.Recognizer()
        while True:
            with sr.Microphone(device_index=input_device) as source:
                print("Say something: ")
                audio = r.listen(source)
            try:
                print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
                if "exit" in r.recognize_google(audio).lower():
                    print("Exiting...")
                    break
                speechDetector.text_to_speech(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not undestrand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def text_to_speech(text):
        engine = pyttsx3.init()
        engine.say(text.lower())
        engine.runAndWait()

        
            