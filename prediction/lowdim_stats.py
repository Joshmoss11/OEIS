import os
import sys
import numpy as np
import prediction.oeis_filter as oif
import prediction.oeis_io as oio
import matplotlib.pyplot as plt

__author__ = "Yoav Wald, Ofer Springer"

if __name__ == "__main__":
    """
    Running this file generates figures of some low dimensional statistics (collected over
    the filtered sequences) which we will later use to evaluate the predictive power of the CNN  -

    - histogram of overall digits.
    - histogram of LSD of 30'th number in sequence.
    - histogram of LSD of 31'st number in sequence.
    - joint histogram of (LSD of 30'th number, LSD of 31'st number).

    - histogram of overall log10(1+abs(number in seq.)).
    - histogram of log10(1+abs(30'th number in seq.)).
    - histogram of log10(1+abs(31'st number in seq.)).
    - joint histogram of (1+abs(log10(30'th number in seq.)), 1+abs(log10(31'st number in seq.))).

    - overall sequence label histogram.
    - joint histogram of (1+abs(log10(30'th number in seq.)), sequence label).
    """

    script_fn = os.path.abspath(sys.argv[0])
    script_dir = os.path.dirname(script_fn)
    oeis_dir = os.path.dirname(script_dir)
    seq_vals_fn = os.path.join(oeis_dir, 'data', 'stripped')
    digit_mats_fn = os.path.join(oeis_dir, 'data', 'digit_mats')

    seqs, _, _ = oio.read_seq_values(seq_vals_fn)
    seq_vals = oif.filter_short_seqs(seqs)
    digit_mats = oio.read_seq_digit_mats(digit_mats_fn)
    digit_mats = oif.filter_short_digit_mats(digit_mats)

    vals_all = np.concatenate(seq_vals)
    vals_29 = np.array([val[29] for val in seq_vals])
    vals_30 = np.array([val[30] for val in seq_vals])

    fig = plt.figure()
    plt.hist(digit_mats.flatten(), log=True)
    fig.suptitle('Histogram of all digits in filtered sequences')
    fig = plt.figure()
    plt.hist(digit_mats[:, 29, 0])
    fig.suptitle("Histogram of least-significant-digit of 30'th number in filtered sequences")
    fig = plt.figure()
    plt.hist(digit_mats[:, 30, 0])
    fig.suptitle("Histogram of least-significant-digit of 31'st number in filtered sequences")
    fig = plt.figure()
    H, x, y = np.histogram2d(digit_mats[:, 29, 0], digit_mats[:, 30, 0])
    plt.imshow(np.log10(H), interpolation='nearest')
    fig.suptitle("Joint log-frequency of least-significant-digits of 30'th and 31'st number in filtered sequences")

    fig = plt.figure()
    plt.hist(np.log10(1+np.abs(vals_all)), log=True)
    fig.suptitle('Histogram of log10(1+abs(number in seq.)) in filtered sequences')
    fig = plt.figure()
    plt.hist(np.log10(1+np.abs(vals_29)), log=True)
    fig.suptitle("Histogram of log10(1+abs(30'th number in seq.) in filtered sequences")
    fig = plt.figure()
    plt.hist(np.log10(1+np.abs(vals_30)), log=True)
    fig.suptitle("Histogram of log10(1+abs(31'st number in seq.) in filtered sequences")
    fig = plt.figure()
    H, x, y = np.histogram2d(np.log10(1+np.abs(vals_29)), np.log10(1+np.abs(vals_30)))
    plt.imshow(np.log10(H), interpolation='nearest')
    fig.suptitle("Joint log-histogram of log10(1+abs(30'th val) and log10(1+abs(31'st val) in filtered sequences")

    plt.show()