#array_dtw_dist writes dtw distances for the given mfcc or plp matrix to file as computed by DTW_cosines.py
#inputs: matrix of plps or mfccs, and must manually write file to write to
#outputs: matrix containing dtws of all elements in input matrix compared with each other, also writes to specified file
import Consonant_filemaker as cf
import DTW_cosines as dc
import numpy as np

file = open('dtw_mfcc_matrix.txt', 'w') 

def array_dtw_dist(plplist):

    cosines_matrix = []
    dtw_matrix = []
    p = 0

    #create mfcc cosines/DTW distances
    for i in plplist:
        mfcc1 = np.transpose(plplist[i])
        sub_matrix = [] #cosines matrix
        sub_matrix2 = [] #DTW distance matrix
        for j in plplist:
            mfcc2 = np.transpose(plplist[j])
            if(len(mfcc1[0]) == len(mfcc2[0])):
                dtw_distance = dc.calculate_normalized_dtw_distance(mfcc1, mfcc2)#compute the DTW
                
            sub_matrix2.append(dtw_distance)
        
        file.write(str(i) + ": " + str(sub_matrix2) + "\n")#write to file

        dtw_matrix.append(sub_matrix2)#this matrix contains whats written in the fil eif one desires 
        p = p + 1
        print (p)

    return dtw_matrix

#choose desired input
MFCCarray = cf.embeddingsmaker()[0]
# PLParray = cf.embeddingsmaker()[1]
 
#specify desired input and call function
array_dtw_dist(MFCCarray)