#DTW_cosines computes the dynamic time warping distance between two mfccs or plps
#inputs: two mfccs or plps with the same dimension[1]
#outputs: a single value represneting the DTW distance between the inputs

import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from sklearn.metrics.pairwise import cosine_similarity

def calculate_normalized_dtw_distance(mfcc1, mfcc2):
    distance, _ = fastdtw(mfcc1, mfcc2, dist=euclidean)
    normalized_distance = distance / max(len(mfcc1), len(mfcc2))
    return normalized_distance


#example for testing purposes: 

# Example usage
# mfcc1 = np.array([[-3.84110535e+02, -3.96513397e+02, -4.99617462e+02, -5.06676605e+02],
#                   [1.58165192e+02, 1.59340912e+02, 1.65728058e+02, 1.09907753e+02],
#                   [2.34497299e+01, 1.13249397e+01, 1.57546082e+01, -1.75710850e+01]])
# mfcc2 = np.array([[4.94295597e+00, -5.27101231e+00, -1.03837032e+01, 1.08313894e+01],
#                   [3.07199240e+00, 4.54174042e+00, 9.73814583e+00, 1.58587780e+01],
#                   [-1.95688248e+01, -1.75259018e+01, -6.97885036e+00, -7.78309727e+00]])

# dtw_distance = calculate_normalized_dtw_distance(mfcc1, mfcc2)
# cosine_sim = calculate_cosine_similarity(mfcc1, mfcc2)

# print("Normalized DTW Distance:", dtw_distance)
# print("Cosine Similarity:", cosine_sim)
