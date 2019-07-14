#!/usr/bin/python
# -*- coding: UTF-8 -*-

from dimsim import get_distance, getCandidates
from dtw import dtw
import matplotlib.pyplot as plt


def get_sentence_distance(s1, s2):
    # We define two sequences x, y as numpy array
    # where y is actually a sub-sequence from x
#     x = np.array([2, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
#     y = np.array([1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
    # Here, we use L2 norm as the element comparison distance
    phonetic_norm = lambda x, y: min(get_distance(x, y), 10)
    
    dist, cost_matrix, acc_cost_matrix, path = dtw(s1, s2, dist=phonetic_norm, warp=1)

#     plt.imshow(acc_cost_matrix.T, origin='lower', cmap='Blues', interpolation='nearest')
#     plt.plot(path[0], path[1], 'w')
#     plt.show()
    return dist

if __name__ == "__main__":
#     dis = get_distance("较兰", "兰花")
#     print(dis)
    
    dis = get_sentence_distance("德华的忘情水", "忘情水")
    print(dis)
#     dis = get_sentence_distance("兰花", "播放兰花")
#     print(dis)
#     dis = get_sentence_distance("兰花", "兰色的花")
#     print(dis)
#     dis = get_sentence_distance("兰花", "兰色花")
#     print(dis)
#     dis = get_sentence_distance("兰花", "蓝花")
#     print(dis)
#     sentence = "播放忘情水"
#     cw = getCandidates(sentence)
#     print(cw)