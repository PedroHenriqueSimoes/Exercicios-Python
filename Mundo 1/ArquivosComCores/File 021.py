from pygame import mixer

mixer.init()
mixer.music.load('File021.mp3')
mixer.music.play()
input('\033[31mAperte enter para finalisar:\033[m ')
