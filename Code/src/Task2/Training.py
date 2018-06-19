# Embedded file name: /home/ubuntu/Desktop/Training.py
import Gesture_Recognition as code
import numpy as np
from sklearn import svm
X = np.empty([code.number_of_training_samples, code.total_features], dtype=float)
for n in range(0, code.number_of_training_samples):
    feature_count = 0
    for a in range(0, code.axis):
        for i in range(0, code.kmax):
            for j in range(0, code.number_of_features):
                X[n, feature_count] = code.gesture[n, a, i, j]
                feature_count = feature_count + 1