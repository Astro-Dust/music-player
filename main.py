import vlc
import time
import os

def song_options(player):
    while True:
        try:
            option = input("""
SONG OPTIONS:

[1] PAUSE        
[2] STOP

> """).strip()

            if option == '1':
                os.system('clear || cls')
                if player.is_playing():
                    player.pause()
                    while True:
                        option = input("""
SONG OPTIONS:

[1] CONTINUE
[2] STOP

> """).strip()
                        if option == '1':
                            player.pause()  # Mesmo método usado para tocar e pausar
                            time.sleep(1)
                            os.system('clear || cls')
                            return
                        elif option == '2':
                            player.stop()
                            return
                        else:
                            os.system('clear || cls')
                            print("Invalid option.")
            elif option == '2':
                player.stop()
                return
            else:
                os.system('clear || cls')
                print("Invalid option.")
        except ValueError:
            os.system('clear || cls')
            print("Invalid input.")

music_name = 'songs/Coffee.mp3'
player = vlc.MediaPlayer(music_name)

player.play()

# Esperando 1 segundo para dar tempo da música iniciar
time.sleep(1)

while player.is_playing():
    song_options(player)
    
print("Music finished.")
