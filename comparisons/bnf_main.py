#bnf_main computes and writes to file the cosines from bnfs contained in a txt file
#inputs: txt file with filenames and bnfs
#outputs: none, but writes bnf cosines to file 

from audio_separation.find_relevantcs import create_consonant_matrix as cons_matrix
from audio_separation.ratings_matrix import ratings_matrix
from audio_separation.highestvals_matrix import highestvals_matrix
from audio_separation.lowestvals_matrix import lowestvals_matrix
import csv

fwrite = open('high_to_difflow_bnfcos.txt', 'a')

#find_value_in_csv finds the line number in the given file that contains both input strings
#inputs: filename, and two strings to find
#outputs: the line number that contains both strings in the file, or None if no such line exists
def find_value_in_csv(file_path, string1, string2):
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if string1 in row and string2 in row:
                # print(str(float(row[-2])))
                return float(row[-2])  # Convert the value to a float and return it
    return None

def main(): 
    
    file_name = "out_cosines (1).csv"  # Replace with the actual CSV file name
    
    rating_matrix = ratings_matrix("i_trans_items_buck.txt")#create matrix with consonants and their ratings
    highest_matrix = highestvals_matrix(rating_matrix, 0.8)#create matrix with only consonants with >=0.8 ratings
    lowest_matrix = lowestvals_matrix(rating_matrix, 0.13)#create matrix with only consonants with <= 0.3 ratings

    #for every one in highest matrix, find number of other highest, get cosine for compared to highest in ratings matrix
    for i in highest_matrix:
            name1 = i[0] + ".wav"#get audio's name
            for j in lowest_matrix:
                if(i[1] != j[1]):
                    name2 = j[0] + ".wav"
                    bnfcosine = find_value_in_csv(file_name, name1, name2)
                    if (bnfcosine != None):
                        #print for testing purposes and write to file with format (filename1 (rating), filename2(rating): bnf cosine)
                        print(name1 + "(" + str(i[2]) + "), " + name2 +  "(" + str(j[2]) + "): " + str(bnfcosine) + "\n")
                        fwrite.write(name1 + "(" + str(i[2]) + "), " + name2 +  "(" + str(j[2]) + "): " + str(bnfcosine) + "\n")

    fwrite.close()
    
if __name__ == "__main__":
    main()
