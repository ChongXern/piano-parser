import librosa 

class PianoNote:
    def __init__(self, pianoNote, freq, pxStart, pxEnd):
        self.pianoNote = pianoNote
        self.freq = freq
        self.pxStart = pxStart
        self.pxEnd = pxEnd
    
