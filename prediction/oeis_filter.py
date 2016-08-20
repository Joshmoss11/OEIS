""" TODO: nothing here yet """
import numpy as np


def filter_short_digit_mats(mats):
    """ filters sequences where we do not know or have the first 31 numbers """
    good_samples = np.array([],dtype="int32")
    for i in range(len(mats)):
        if np.all(mats[i, :, :]<255):
            good_samples = np.append(good_samples,[int(i)])
    return mats[good_samples, :, :]


def filter_short_seqs(seqs):
    """ filters sequences where we do not know or have the first 31 numbers """
    return [seq for seq in seqs.values() if len(seq) >= 31]
