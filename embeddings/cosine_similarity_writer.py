#cosine_similarity writer is used to write both plp and mfcc cosines to txt file
#inputs: a plp or mfcc array 
#outputs: none, but it writes all the cosines between all the entries of the plp or mfcc array to a txt file

from audio_separation.ratings_matrix import ratings_matrix as ratings
from audio_separation.highestvals_matrix import highestvals_matrix as highvals
import Consonant_filemaker as cf
from cosine_similarity import get_cosine
import DTW_cosines as dc
import numpy as np

file = open('cosine_plp_matrix.txt', 'a') 

def array_dtw_dist(plplist):

    cosines_matrix = []
    p = 0

    #create mfcc cosines/DTW distances
    #iterate through every element in input array
    for i in plplist:
        mfcc1 = np.transpose(plplist[i])#transpose for cosine computation
        sub_matrix2 = [] #cosine matrix
    
        #iterate through every elemnt in input array
        for j in plplist:
            mfcc2 = np.transpose(plplist[j])#transpose for cosine computation
            cosine_similarity = get_cosine(mfcc1, mfcc2)#compute cosine for two mfccs     
            sub_matrix2.append(cosine_similarity)#put in matrix for this iteration
            
        file.write(str(i) + ": " + str(sub_matrix2) + "\n")#write matrix to file in one line

        cosines_matrix.append(sub_matrix2)#append to return matrix
        p = p + 1
        print (p)

    return cosines_matrix#can return th ematrix as well if desired

#whichever one desired as input can be created (for efficiency's sake, comment out the other)
# MFCCarray = cf.embeddingsmaker()[0]
PLParray = cf.embeddingsmaker()[1]
 
#call the function with desired input
array_dtw_dist(PLParray)

file.close()