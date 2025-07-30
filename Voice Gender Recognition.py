import librosa

def extract_features(file):
    y, sr = librosa.load(file)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return mfcc.mean(axis=1)

print("Voice features extracted.")
