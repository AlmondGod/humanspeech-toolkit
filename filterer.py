#Given a written txt file of comparisons such as "cosine_mfcc_matrix", filterer 
#writes a new script comparing only identical talkers (now modified to be identical talkers and sessions) to each other
#inputs: txt file with format: filename(rating), filename(rating): cosine/dtwdist
#outputs: filtered txt file (refined and p_refined txt files)

def extract_speaker(line):
    # Split the line based on '_'
    parts = line.split('_')
    speaker = parts[3][0:3]
    return speaker

def extract_speaker2(line):
    # Split the line based on '_'
    parts = line.split('_')
    speaker = parts[8][0:3]
    return speaker

def filter_lines_by_speaker(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Extract the speaker from the first line
    reference_speaker = extract_speaker(lines[0])

    file = open(output_file, 'w')
    file.write("format: vowel1.cons_vowel2_set_talker+session_startingtime_30f(rating), vowel1.cons_vowel2_set_talker+session_startingtime_30f(rating): cosine\n")
    print("start")

    for line in lines:
        # print(extract_speaker(line) + ", " + extract_speaker2(line) + "\n")
        if(extract_speaker(line) == extract_speaker2(line)):
            print(extract_speaker(line) + ", " + extract_speaker2(line) + "\n")
            
            file.write(line)

    print("done")
# Replace 'input.txt' with the path to your input file and 'output.txt' with the desired output file path.
input_file = 'high_to_diffhigh_plpdtw.txt'
output_file = 'p_refined_h2dhplpdtw.txt'
filter_lines_by_speaker(input_file, output_file)
