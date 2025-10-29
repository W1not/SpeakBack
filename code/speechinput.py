import speech_recognition as sr
import pyaudio
import os

class speechDetector:
    def speech_search():
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            list_device = p.get_device_info_by_index(i)
            if list_device["maxInputChannels"] >= 1:
                print("Microfono ",  list_device["index"] , " " , list_device["name"])

    def speech_configurator(index,output):
        print(index)
        print(output)

    def speech_usage():
        r = sr.Recognizer()
        with sr.Microphone as source:
            print("Say something: ")
            audio = r.listen(source)

        try:
            r = sr.AudioSource()
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        
            