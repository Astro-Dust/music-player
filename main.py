import vlc
import time
import os

def song_options():

    option = int(input("""
    SONG OPTIONS:
    
    [1] PAUSE        
    
    [2] STOP

    > """))

    match(option):
        case 1:
            os.system('clear')
            if player.is_playing:
                player.pause()
                option = int(input("""
    SONG OPTIONS:

    [1] CONTINUE

    [2] STOP

    > """))

            if option == 1:
                player.pause() # mesmo método usado pra tocar e pausar (???)
                time.sleep(1)
                os.system('clear')
            elif option == 2:
                player.stop()
            else:
                print("Invalid option.")

        case 2:
           player.stop()

music_name = 'songs/de_nio_namnen.mp3'
player = vlc.MediaPlayer(music_name)

player.play()

# esperando 1 segundo para dar tempo da música iniciar
time.sleep(1)

while player.is_playing():
    song_options()
    
print("Music finished.")

