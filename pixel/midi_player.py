import pygame as pg

def load_file(file_name):
    try:
        music_file = file_name
        freq = 44100    # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 2    # 1 is mono, 2 is stereo
        buffer = 1024    # number of samples
        pg.mixer.init(freq, bitsize, channels, buffer)
        pg.mixer.music.load(file_name)
    except pg.error:
        print("File %s not found! (%s)" % (file_name, pg.get_error()))

def stop():
    pg.mixer.music.stop()

def play():
    pg.mixer.music.play()
