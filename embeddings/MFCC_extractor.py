#given a .wav file, MFCC_extractor.extract returns an array with the audiofile's MFCC as computed by librosa
#inputs: .wav file
#outputs: MFCC array
import librosa
import numpy as np

def extract(filepath):

    #set path to audio file
    audio_file_path = filepath

    # Load the audio file
    audio, sample_rate = librosa.load(audio_file_path)

    #compute mfcc
    mfcc = librosa.feature.mfcc(y=audio, sr=22050)
    
    # print('MFCC: ', mfcc) #print mfcc for testing purposes 
    return mfcc

# Example use:
# wav_file = "s0401a_f_364.241854_364.410647.wav"
# mfcc_features = extract(wav_file)
# print(mfcc_features)
