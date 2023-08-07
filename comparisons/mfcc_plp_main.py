#mfcc_plp_main is the 'main' function of this whole program for mfccs and plps. 
    #it writes txt files which are arrays of cosines between the mfccs or plps 
    #of highly rated vs highly rated audiofiles of the same consonant, highly rated vs lowly rated audiofiles of different consonants, and every other combination 
    #It can be adjusted to compute highest vs highest, highest vs lowest, etc. but adjusting the highest_matrix and lowest_matrix in the for loops
#inputs: none, but you must have a files containing the matrix of cosines to compare, and a file to write to 
#outputs: none, but it writes to the output file
from audio_separation.find_relevantcs import create_consonant_matrix as cons_matrix
from audio_separation.ratings_matrix import ratings_matrix
from audio_separation.highestvals_matrix import highestvals_matrix
from audio_separation.lowestvals_matrix import lowestvals_matrix
import linecache

file = open('cosine_mfcc_matrix.txt', 'r') 
fwrite = open('high_to_low_mfcccos.txt', 'a') 

#find_matching_line finds the line number of the audio file with the given inputs
#inputs: filename, consonant, timing, and speaker/session
#outputs: line number of corresponding audiofile, of None if no corresponding audiofile is in the txt file
def find_matching_line(filename, consonant, timing, audioname):
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, 1):
            parts = line.strip().split('_')
            if len(parts) == 4:
                filen, file_consonant, file_timing = parts[0], parts[1], parts[2]
                if filen == audioname and file_consonant == consonant and round(float(file_timing), 1) == round(float(timing), 1):
                    return line_number
    return None

#file_val finds the corresponding cosine of two plps in txt files such as cosine_plp_matrix and cosine_mfcc_matrix
#inputs: txt file to read from, which line in the txt file to go to (representing frist audiofile in the cosine), and which value in the array on that line (representing second audiofile) to return
#outputs: the corresponding cosine from the inputs 
def file_val(file_path, line_number, array_index):
    try:
        line = linecache.getline(file_path, line_number).strip()
        if line:
            parts = line.split(': ')
            if len(parts) == 2:
                values = eval(parts[1])  # Safely evaluate the string as a Python list
                if array_index >= 0 and array_index < len(values):
                    return values[array_index]
                else:
                    return None
        return None
    except IndexError:
        return None
    

def main():
    
    rating_matrix = ratings_matrix("txt_files/i_trans_items_buck.txt")#create matrix with consonants and their ratings
    highest_matrix = highestvals_matrix(rating_matrix, 0.8)#create matrix with only consonants with >=0.8 ratings
    lowest_matrix = lowestvals_matrix(rating_matrix, 0.13)#create matrix with only consonants with <= 0.3 ratings

    p = 0
    #for every one in highest matrix, find number of other highest, get cosine for compared to highest in ratings matrix
    for i in highest_matrix:
        if (p > 2):
            audiofilename = i[0].strip().split('_')[3]#get audio's filename
            cons = i[1]#get what consonant it is
            time = i[0].strip().split('_')[4]#get timing
            line1 = find_matching_line('cosine_mfcc_matrix.txt', cons, time, audiofilename)#get what number in document it is
            for j in lowest_matrix:
                if (cons == j[1] and j != i):#if consonants are the same but not same exact entry

                    audiofilename2 = j[0].strip().split('_')[3]#get audio's filename
                    cons2 = j[1]#get what consonant it is
                    time2 = j[0].strip().split('_')[4]#get timing
                    line2 = find_matching_line('cosine_mfcc_matrix.txt', cons2, time2, audiofilename2)#get what number in document second is
                    
                    #if we have both valid audiofiles with complete information:
                    if (line1 != None and line2 != None):
                        targetline = file_val('cosine_mfcc_matrix.txt', line1, line2)

                        #print cosine and corresponding audiofile names for testing purposes
                        print(i[0] + "(" + i[2] + "), " + j[0] +  "(" + j[2] + "): " + str(targetline))

                        #write to file
                        fwrite.write(str(i[0]) + "(" + str(i[2]) + "), " + str(j[0]) +  "(" + str(j[2]) + "): " + str(targetline) + "\n")
        p = p + 1

    file.close()
    fwrite.close()

if __name__ == "__main__":
    main()
