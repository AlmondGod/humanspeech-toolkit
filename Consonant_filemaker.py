#embeddingsmaker is a multiuse file that 
    #1. creates the shorter .wav files from the larger overall file (this is currently disabled as the function must only be performed once)
    #2. creates mfcc and plp matrices from those .wav files
    #3. writes those matrices to file
#inputs: 1. .wav files and a txt file containing start and end times and, if desired, other metadata about the files
#outputs: 
from pydub import AudioSegment
import find_relevantcs
import numpy as np
import MFCC_extractor as mfcc
import PLP_extractor as plp
from DTW_cosines import calculate_normalized_dtw_distance as dtw
from DTW_cosines import calculate_cosine_similarity as cos

def embeddingsmaker():
    input_file = "code/s0401a.wav"
    info_file = "code/myoutaug8.txt"

    mfcc_matrix = {} #dictionary with (filename, mfcc)
    plp_matrix = {} #dictionary with (filename, plp)

    #create matrix with relevant consonants
    #(consonant, duration, timing, file)
    global relevantcs_matrix
    relevantcs_matrix = find_relevantcs.create_consonant_matrix("code\i_trans_items_buck.txt")
    
    # Read consonant information from the text file iterating through each line
    # (file, end time, consonant)
    global consonant_info
    consonant_info = []
    with open(info_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                cols = line.split()
                consonant = cols[2]
                end_time = float(cols[1]) * 1000    
                audio_file = cols[0]
                consonant_info.append((consonant, end_time, audio_file))
                
    trackcounter = 0;  
    # Clip audio based on consonant information and create mfccs and plps
    for i, (consonant, end_time, audio_file) in enumerate(consonant_info):
        #make sure clip is a consonant
        if(consonant == "b" or consonant == "c" or consonant == "ch" or consonant == "d" or consonant == "dh" or consonant == "dx"
                   or consonant == "f" or consonant == "g" or consonant == "hh" or consonant == "jh" or consonant == "k" or consonant == "l" 
                   or consonant == "m" or consonant == "n" or consonant == "nx" or consonant == "p" or consonant == "tq" or consonant == "r" 
                   or consonant == "s" or consonant == "sh" or consonant == "t" or consonant == "th" or consonant == "tq"  or consonant == "v" 
                   or consonant == "w" or consonant == "y" or consonant == "z"  or consonant == "zh"):
            if i > 0:
                start_time = consonant_info[i-1][1] 
            else:
                start_time = 30

            # Add 30ms on each side
            start_time -= 30
            end_time += 30

            #format start and end times for filename (convert to seconds, and cut off at 6 decimal places)
            initstart = start_time /1000
            initend = end_time / 1000
            starttname = format(initstart, ".{}f".format(min(6, len(str(initstart).split(".")[1]))))
            endtname = format(initend, ".{}f".format(min(6, len(str(initend).split(".")[1]))))
            starttname = float(starttname)
            endtname = float(endtname)
            input_file = "code/" + audio_file + ".wav"
            
            #print filename and create actual file
            output_file = f"{audio_file}_{consonant}_{starttname}_{endtname}.wav"

            #create audiofiles and print if desired. 
            for row in relevantcs_matrix:
                if(audio_file == row[3] and consonant == row[0]):
                    # The padding of 0.04 for checking if the consonant is relevant is somewhat arbitrary, but ensures subjectively decent accuracy.
                    # (the padding might desirably be adjusted to 0.162 (based on getting closest to the number 1916 (number of audiofiles in i_trans_items_buck.txt))
                    if(starttname > row[2] - 0.04 and endtname < row[2] + row[1] + 0.04):
                        # clip_audio(input_file, output_file, start_time, end_time)
                        # print(str(trackcounter) + " " + f"Clipped audio for consonant '{consonant}' from {start_time}ms to {end_time}ms and saved as '{output_file}'." + "|| " + str(row[2]))
                        trackcounter += 1
                        # mfcc_matrix[output_file] = mfcc.extract(output_file)
                        
                        plp_matrix[output_file] = plp.extract(output_file)

    # with open('plp_matrix.txt', 'w') as convert_file:
    #     convert_file.write(str(plp_matrix))
    return (mfcc_matrix,plp_matrix)


#clip_audio creates a shortened audio clip from a longer .wab audio file
#inputs: subclip filename, original filename, start and end times for the subclip 
#outputs: none, but created a .wav file as specified
def clip_audio(input_file, output_file, start_time, end_time):
    audio = AudioSegment.from_wav(input_file)
    clipped_audio = audio[start_time:end_time]
    clipped_audio.export(output_file, format="wav")

#getter methods for the important matrices from consonant_filemaker
def getconsonant_matrix():
    return consonant_info

def getrelevantcs_matrix():
    return relevantcs_matrix

#simple write array to file function
def write_array_to_file(array, filename):
    with open(filename, 'w') as file:
        for item in array:
            file.write(str(item) + '\n')

#simple make array from file function
def read_file_to_array(array, filename):
    with open(filename, 'r') as file:
        for line in file:
            array.append(line)

#calling main function
x = embeddingsmaker()

