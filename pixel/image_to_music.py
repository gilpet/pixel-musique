from PIL import Image
from midiutil.MidiFile import MIDIFile
from django.core.exceptions import ValidationError

def file_size(value):
    limit = 100 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 100 KB.')

def get_image_data(img):
    return list(Image.open(img).getdata())

def rgb_to_midi(rgb):
    return 21 + (rgb % 87)

def pixels_to_midi(pix, image_name):
    try:
        mf = MIDIFile(1)
        track = 0
        time = 0
        channel = 0
        volume = 100
        mf.addTrackName(track, time, image_name)
        mf.addTempo(track, time, 1000)
        for i in pix:
            p2 = rgb_to_midi(i[1])
            p3 = rgb_to_midi(i[2])
            duration = 1
            if time % 4 == 0:
                mf.addNote(track, channel, p2, time, 4, volume)
                mf.addNote(track, channel, p3, time, 4, volume)
            else:
                mf.addNote(track, channel, p3, time, duration, volume)
            time += 1
        with open(image_name, 'wb') as outf:
            mf.writeFile(outf)
        return len(pix)
    except Exception as e:
        print(e)
