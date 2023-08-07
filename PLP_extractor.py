#given a .wav file, PLP_extractor.extract returns an array with the audiofile's PLP as computed by rasta
#inputs: .wav file
#outputs: PLP array
import librosa
import numpy as np
import rasta

def extract(filename):
    # Load WAV file
    file_path = filename
    x, sr = librosa.load(file_path, sr=None)
    # Compute PLP features
    plp_features = rasta.rastaplp(x, sr)
    # print(plp_features) #print for testing purposes

    return plp_features
