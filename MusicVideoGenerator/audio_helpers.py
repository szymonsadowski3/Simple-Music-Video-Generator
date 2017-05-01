import librosa


def estimateTempo(audio_path):
    print('Estimating tempo of {}'.format(audio_path))
    y, sr = librosa.load(audio_path)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    return tempo[0]

def getDuration(audio_path):
    y, sr = librosa.load(audio_path)
    return librosa.get_duration(y=y, sr=sr)