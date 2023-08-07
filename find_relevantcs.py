#this function goes through a txt file of relevant vowel-consonant-vowel files
#(here, we use i_trans_items_buck.txt), and creates a matrix with consonants, 
#their timings, their durations, and what file they're in

def create_consonant_matrix(file_path):
    consonant_matrix = []
    visited_consonants = set()
    with open(file_path, 'r') as file:
        line_skipper = 0

        #iterate through lines in the file
        for line in file:
            if (line_skipper > 0):
                line_skipper -= 1
                continue
            line = line.strip().split('\t')

            #get duration, what consonant it is, and its timing
            duration = float(line[8])
            middle_consonant = line[2]
            timing = float(line[15])

            #get what section its in (ex s0401a)
            initsection = line[0].split("_")
            section = initsection[3]
            consonant_tuple = (middle_consonant, duration, timing, section)

            #put it in return matrix if its not a repeat, then skip the next 23 lines cause they should be identical
            if consonant_tuple not in visited_consonants:
                consonant_matrix.append(consonant_tuple)
                visited_consonants.add(consonant_tuple)
                line_skipper = 22
            #print each line for testing purposes
            print(consonant_tuple)
    return consonant_matrix