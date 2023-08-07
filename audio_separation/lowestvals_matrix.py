#This function, given a ratings_matrix and a threshold value, returns a 2D array containing all the audiofiles
#with ratings below the threshold. Each row of the array consists of the audiofile's name, the 
#lowest-value consonant, and this consonant's agreement value.

def lowestvals_matrix(ratings_matrix, threshold):

    #create new 2D array with the filename, consonant, and rating
    lowestvals_ratings = [[""]*3]*1

    #instantiate highestvals_ratings matrix iterator
    j = 1

    #iterate through ratings-matrix and only pull values greater than threshold into new matrix
    for i in range(1, int(len(ratings_matrix) / 2.5)):

        #if the current row entry's agreement value is greater than the threshold,
        if ( float(ratings_matrix[i][2]) < threshold):

            #add this entry to our new 2D matrix
            lowestvals_ratings.append(ratings_matrix[i])

            #print (nicely formatted) row for testing purposes
            print(lowestvals_ratings[j][0] + ": " + lowestvals_ratings[j][1] + ", " + lowestvals_ratings[j][2])
            
            #increment highestvals_ratings matrix iterator
            j += 1

    #get rid of empty first row from instatiation
    lowestvals_ratings.pop(0)

    return lowestvals_ratings