import speechinput as sp

if __name__ == "__main__":
    sp.speechDetector.speech_search()
    index = int(input("Index "))
    output = int(input("Output "))

    sp.speechDetector.speech_configurator(index,output)
    sp.speechDetector.speech_usage()