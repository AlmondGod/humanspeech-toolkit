#function that turns a file with consonants and ratings into matrix with rows as all instances of file-consonant pairings 
    #with nonzero agreement, with each row consisting of filename, consonant measured, and agreement
#inputs: link to file you want to turn into ratings matrix
#outputs: 3-column array with each row having: filename, consonant, and corresponding agreemnet rating
def ratings_matrix(filelink):
    #open file
    f = open(filelink, "r")

    #create 2D array with filename, consonant, agreement value as columns
    consonant_ratings = [[""]*3]*1

    #iterate through each line
    i = 1
    for line in f:

        #get value for percent agreement
        init_value = nth_substring(line, "	", 3)
        agreement_value = init_value[0: init_value.index("	")]

        #can print the value of the agreement for testing purposes
        #print(agreement_value)

        #if value of agreement for consonant is not 0
        if(agreement_value.__contains__("1") or agreement_value.__contains__(".")):

            #create temporary list to store row of values (filename, consonant, rating)
            templist = [""] * 3

            #get filename of consonant
            filename = line[0:line.index("	")]

            #put filename in first column of entry
            templist[0] = filename
            
            #get what consonant we're on
            subline = line[line.index("	") + 1:]
            templist[1] = subline[0:subline.index("	")]
            
            #get % of how many people agreed it was this consonant
            subs = nth_substring(subline, "	", 2)
            templist[2] = subs[0: subs.index("	")]
            
            #put list into 2D matrix
            consonant_ratings.append(templist)

            #can print (filename, consonant, rating) for each iteration for testing purposes
            # print (consonant_ratings[i][0] + ": " + consonant_ratings[i][1] + ", " + consonant_ratings[i][2])

            #increment i
            i += 1
            
    #close file
    f.close()

    #get rid of empty first row from instatiation
    consonant_ratings.pop(0)

    return consonant_ratings

#finds nth instance of a substring in a given string
def nth_substring(string, substring, n):
    for i in range(0, n):
        string = string[string.index(substring) + 1: ]
    return string