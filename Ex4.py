from converter import Converter
conv = Converter()

info = conv.probe('bbb.avi')

#here, we specify the new codecs and also the new type of file
convert = conv.convert('bbb.avi', 'bbb.mp4', {
    'format': 'mp4',
    'audio': {
        'codec': 'aac', #change of codec
        'samplerate': 11025,    #new audio properties
        'channels': 2
    },
    'video': {
        'codec': 'AVS',    #change of codec
        'width': 720,   #new video properties
        'height': 400,
        'fps': 25
    }})
