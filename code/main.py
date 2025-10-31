import speechinput as sp
import menu

if __name__ == "__main__":
    detector = sp.speechDetector()
    detector.list_input_devices()
    # input_device = int(input("Index "))
    # output_device = int(input("Output "))
    menu.GUI().run()
    # sp.speechDetector.speech_usage(input_device)