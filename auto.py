from PIL import Image,ImageGrab
import pyautogui
import pyttsx3
import time

engine = pyttsx3.init("sapi5")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    for i in range(310, 410):
        for j in range(375, 450):
            if data[i, j] < 150:
                hit('up')
                return
    for i in range(300, 380):
        for j in range(320, 380):
            if data[i, j] < 150:
                hit('down')
                return

    return

if __name__ == "__main__":
    speak("Hello your dino game is about to start in 2 seconds")
    time.sleep(1)

while True:
    # time.sleep(2)
    image = ImageGrab.grab().convert('L')
    data = image.load()
    isCollide(data)
# drawing rectangle for cactus

# image = ImageGrab.grab().convert('L')
# data = image.load()

# for i in range(250,330):
#     for  j in range(390,450):
#         data[i,j] = 0
# for i in range(250, 330):
#     for j in range(320, 390):
#         data[i, j] = 150



# image.show()

# image.show()
