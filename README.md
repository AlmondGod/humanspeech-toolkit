# FILE PURPOSES:

### Audio Processing
##### .wav minifiles creation

The main file in this program that takes a buckeye .wav file and a .txt file with the end times of every consonant 
and outputs individual .wav files for all the consonants, (Here, the txt file is myoutaug8.txt and the wav files are s0401a.wav through s0404a.wav), 
but filters and outputs only the consonant audiofiles for the relevant consonants based on i_trans_items_buck.txt.

Calls find_relevantcs.create_consonant_matrix() using i_trans_items_buck to create a matrix of relevant consonants

Naming convention of the files: session_consonant_starttime_endtime
                ex: s0401a_b_34.32145_34.78549

Also has capability to print nicely formatted names and information on the audiofiles

Various parameters, especially the padding on filtering for relevant consonants (currently 0.04) can be changed
    There is a comment about this in the relevant location in consonant_filemaker (towards the bottom)


find_relevantcs.py:
    Has the method create_consonant_matrix
    create_consonant_matrix:
        given a filepath, creates a matrix based on that filepath's text file with rows consisting of 
            (consonant, duration, timing, and what section its in)
            ex: (g, 0.3248, 245.84632, s0401a)

### Embeddings 
##### mfccs, plps, and bnfs
##### dtwdist and cosines
Computes MFCCs, PLPs, DTW distance, cosines for the relevant pairs (relevant meaning only the ones that were rated). The extractors are functions which return embeddings given .wav files as inputs. Cosine similarity writer and DTW distance writer use these to return a single value for a given pair of .wav files with filenames and their corresponding embedding.

### Comparisons
##### the endgame of the toolkit
##### Verifies human ratings with computer-produced cosines and dtw distances

cosine_plp_matrix and cosine_mfcc_matrix are 2D arrays with first column being filenames and second column being an array with the cosine of this file compared to every other file (same order as columns)
dtw_mfcc_matrix.txt and dtw_plp_matrix.txt are plp and mfcc dtw distances formatted the same way as described above
out_cosines (1).csv is a file created by damon luong containing cosines between bnfs of files

high_to_high means comparing highly-rated (>0.8 agreement) consonant files to other highly-rated consonant files of the same consonant. 
    Here we 'aim' for high similarity
    (ex. high_to_high_plpcos is all the plp cosines of highly rated consonants between each other)
high_to_low means comparing highly-rated consonant files to lowly rated (<0.15 agreement) consonant files of the same consonant
    Here we 'aim' for 'decent' similarity
high_to_diffhigh means comparing  highly-rated (>0.8 agreement) consonant files to other highly-rated consonant files of different consonants
    Here we 'aim' for lower similarity than above
high_to_difflow means comparing highly-rated consonant files to lowly rated (<0.15 agreement) consonant files of different consonants
    Here we 'aim' for the lowest similarity, ideally by a 'noticeable' portion

The analysis of these files has not been decided upon, and I'm no expert, but from a quick glance/skim,
some don't seem to conform to expectations/hopes as much as I (to be fair, with no frame of reference) would've expected,
rather all the cosines and even more the dtws seem quite random, for all plps, mfccs, and even bnfs. 
Dr. Swingley, you would know how to analyze the products better than I, so I won't make a conclusion of course. 

Also, certain permutations of the high_to_low vs. high_todifflow etc. and mfcc plp bnf and dtw vs cos, not all these possible combinations of files have been created (this would be 24 files total) have been omitted for times' sake, 
I've tried to include the most 'relevant' ones, focusing on bnfs and cosines, I apologize that I haven't gotten to all of them. 

Explanation of the code files:

code is all commented. main is used to create all the high_to_low etc for mfccs and plps, bnf_main is the same except for bnfs
cosine_similarity_writer was used to make the plp and mfcc cosines, and uses methods from cosine_similarity.py
DTW_cosines was a first attempt but was inaccurate
MFCC_extractor and PLP_extractor were used to make the MFCCs and PLPs for the clipped audiofiles
    librosa was used to create the mfccs and plps
highestvals_matrix and lowestvals_matrix are functions which take in the matrix of audiofiles which have ratings and returns only those above/below a certain threshold respectively
relevantcs_matrix creates an array of all the audiofiles with human-made ratings from i_trans_items_buck.txt

Update on "refined and p_refined" txt files:
These files are "refined" because Dr. Swingley suspected we might find higher average cosines and dtws if we restrict our comparisons
to those where audio1 and audio2 are from the same speaker (ex s39 with s39). These are the p_refined (shortened from partially refined) 
txt files. 

Their filenames are abbreviations of the equivalent unfiltered versions
ex: p_refined_h2dhbnfcos.txt is refined from high_to_diffhigh_bnfcos.txt

I then was curious as to the outcomes of restricting by session as well as speaker (ex s3901a and s3901a). The outcomes of these refinements
are txt files called "refined".
ex: refined_h2dhbnfcos.txt is refined from high_to_diffhigh_bnfcos.txt

### Querying

The format of the refined and p_refined files is:
format: vowel1.cons_vowel2_set_talker+session_startingtime_30f(rating), vowel1.cons_vowel2_set_talker+session_startingtime_30f(rating): cosine

To query the data, one can create an array of strings with all relevant data by splitting the line by '_',
and easily get the relevant cosine by splitting based on ':' (the cosine is always right after this character).
