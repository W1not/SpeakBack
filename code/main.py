import speechinput as sp

if __name__ == "__main__":
    sp.speechDetector.speech_search()
    input_device = int(input("Index "))
    output_device = int(input("Output "))

    sp.speechDetector.speech_configurator(input_device,output_device)
    sp.speechDetector.speech_usage(input_device)