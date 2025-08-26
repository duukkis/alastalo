def loadRaita(mixer, raita):
#  mixer.music.unload()
  mixer.music.load('/home/pi/work/alastalo/raidat/E' + raita  + '.mp3')
  return mixer

def writeMusicPosition(raita, seconds):
  f = open("state.txt", "w")
  f.write(str(raita) + " " + str(seconds))
  f.close()

def loadMusicPosition():
  f = open("state.txt", "r")
  data = f.read()
  return data.split(" ")

