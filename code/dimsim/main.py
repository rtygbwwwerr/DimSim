#!/usr/bin/python
# -*- coding: UTF-8 -*-

from dimsim import get_distance, getCandidates
from dtw import dtw
import matplotlib.pyplot as plt


def get_sentence_distance(s1, s2, max_loc_dis=10.0):
    """
    Computes phonetic distance of two Chinese sentences.
    :param s1: sentence 1
    :param s2: sentence 2
    :param max_loc_dis: the up boundary of local distance 
    Returns the distance between s1 and s2
    """
    
    match_len = min(len(s1), len(s2))
    #we use phonetic similarity as distance 
    #and limit the max distance within 10.0
    phonetic_norm = lambda x, y: min(get_distance(x, y), max_loc_dis)
    #use DTW algorithm for computing sequence distance
    dist, cost_matrix, acc_cost_matrix, path = dtw(s1, s2, dist=phonetic_norm, warp=1)
    #normalize distance with minimum matching length
    dist = dist / (match_len * 2) 
#     plt.imshow(acc_cost_matrix.T, origin='lower', cmap='Blues', interpolation='nearest')
#     plt.plot(path[0], path[1], 'w')
#     plt.show()
    return dist

if __name__ == "__main__":
#     dis = get_distance("较兰", "兰花")
#     print(dis)
    
#     dis = get_sentence_distance("德华的忘情水", "忘情水")
#     print(dis)
    dis = get_sentence_distance("放歌较兰花啊", "兰花")
    print(dis)
#     dis = get_sentence_distance("兰花", "兰色的花")
#     print(dis)
#     dis = get_sentence_distance("兰花", "兰色花")
#     print(dis)
#     dis = get_sentence_distance("兰花", "蓝花")
#     print(dis)
#     sentence = "播放忘情水"
#     cw = getCandidates(sentence)
#     print(cw)