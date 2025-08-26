import time
import functions as f
import pygame
# Import the RPi.GPIO and OS
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def button_callback(channel):
   print("button pressed")

buttonPin = 16
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.add_event_detect(buttonPin,GPIO.RISING,callback=button_callback)

episodes = [
    '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
    '31',
]
eLengths = [
    1200, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0,
    60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0,
    60, 60, 60, 60, 60, 60, 60, 60, 60, 60.0,
    200,
]

# load latest raita
raitaFromFile, secondsFromFile = f.loadMusicPosition()
initTime = float(secondsFromFile)
raita = int(raitaFromFile)
seconds = initTime

# initialize pygame
pygame.mixer.init(frequency=48000)
pygame.mixer = f.loadRaita(pygame.mixer, episodes[raita])
#pygame.mixer.music.play(0, seconds, 2)

def playRaita(raita, initTime, seconds, length):
    playing = False
    while seconds <= length:
        time.sleep(1)

        buttonState = GPIO.input(16)
        print(buttonState)
        if buttonState == GPIO.HIGH and not playing:
            print("play")
            pygame.mixer.music.play(0, seconds)
            playing = True
#        elif buttonState == GPIO.LOW and playing and pause <= 60:
#            pygame.mixer.music.pause()
#            pause = 0
        elif buttonState == GPIO.LOW and playing:
            print("stop")
            seconds = seconds + (pygame.mixer.music.get_pos() / 1000)
            pygame.mixer.music.stop()
            f.writeMusicPosition(raita, seconds)
            playing = False
#        elif buttonState == GPIO.LOW:
#            seconds = (pygame.mixer.music.get_pos() / 1000)

#         if buttonState == GPIO.LOW
#            pause += 1


while True:
#    pygame.mixer.music.play(0, seconds)
    pygame.mixer.music.set_volume(1)
#    print(raita)
#    print(eLengths[raita])
#    pygame.mixer.music.set_volume(1)
    playRaita(raita, initTime, seconds, eLengths[raita])

    raita = (raita + 1) % len(episodes)
    seconds = 0
    initTime = 0
    f.writeMusicPosition(raita, seconds)

    pygame.mixer.music.unload()
    pygame.mixer = f.loadRaita(pygame.mixer, episodes[raita])
#    pygame.mixer.music.play(0, seconds)
