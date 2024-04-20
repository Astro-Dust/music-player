import vlc
import time

music_name = 'songs/de_nio_namnen.mp3'
player = vlc.MediaPlayer(music_name)

player.play()

# esperando 1 segundo para dar tempo da música iniciar
time.sleep(1)

while player.is_playing():
    print("The music is playing.")

print("Music finished.")
