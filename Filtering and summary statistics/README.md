Files
==========
General Usage: default input is the cleaned mat. Otherwise the user can input sequence ID as a vector and the
analysis will be done on these sequence. The results from the functions are ordered in the same way as the input sequences.
For example assume we use the default cleaned_data and the order in cleaned_data is s[eq1 seq2 seq3....] and we are calculating
lengths then the output will be [len1,len2,len3...] where len1 corresponds to seq1,len2 corresponds to seq2 etc.
Alternatively, if the user inputs user ID x,y,z....the we will use seqx,seqy,seqz then the output will be [lenx,leny,lenz...] 
where lenx corresponds to seqx,leny corresponds to seqy etc.

One can extract the extreme sequnces by sorting and saving the original indices using [B,I] = sort(___) where I is the original
indices(see matlab documentation) and then extracting according to index.



[getConverges.m](getConverges.m) - checks whether sequences converges. Convergence is based upon behaviour of the last 10 numbers in the sequence;
We caculate the second order difference on the absolute value of the integers and if all are smaller then 0 we define the sequence as 
converging (if all are equal or smaller then zero then we define the sequencece as inconclusive).
We basically want to see that the difference between numbers (in absolute value) in the sequence is decreasing.
This function will also return the converging sequences

[getDifferences.m](getDifferences.m) - finds the median of differences between adjacent members in a sequence for each sequence
displays the medians that are negative as their absolute value so that they can be displayed in log scale

[getLengths.m](getLengths.m) - gets lengths of each sequence

[getPercentageCubed.m](getPercentageCubed.m) - finds percentage of numbers that are cubed in each sequence. negative numbers are not seen as cubed numbers

[getPercentageSquared.m](getPercentageSquared.m) - finds percentage of numbers that are squares in each sequence. negative numbers are not seen as squared numbers

[getPrimesPercent.m](getPrimesPercent.m) - finds percentage of primes. File s4.mat contains all numbers that are prime in cleaned_data.mat. 
Negative numbers are not considered prime

[getMedianModulo.m](getMedianModulo.m) - finds modulo of first 10 primes for each number in sequence 
Computes median for each number and then for each sequence on aforementioned median
This is done on the OESI cleaned data set(cleaned.mat) and random datasets of size 10000 from the normal and uniform distributions.

[getAverageNumDivisors.m](getAverageNumDivisors.m) - finds sverage number of divisors

[figures](figures) - folder contains all figure created by above scripts/functions


[cleaning_data.m](cleaning_data.m) - Steps we conducted in order to clean the data: 
  (1) Deleted sequences with length<40;
  (2) Deleted duplicates;
  (3) Check for any gaps or non numeric values;
  (4) Deleted fixed sequences;
  (5) Deleted sequences with only 10 different values

[seq_ex.m](seq_ex.m) - examples of different seqs

[hist_appear.m](hist_appear.m)-  checked for multiple appearances in each sequence and computed the median of the occurrences

[monoSeq.m](monoSeq.m) - check for Monotonic sequences

[even_odd.m](even_odd.m) - checked occurrences of even/odd numbers In each sequence

[periodic.m](periodic.m) - checked for periodic sequences

[primeFacFeatSpace.m](primeFacFeatSpace.m) - build a new feature space (more info can be found in the presentation file)

[PCA.m](PCA.m) - Using the feature space we have created, we reduce the dimension space to p=2 using PCA (variance explained = 35%) and plot it

[getSeq.m](getSeq.m)- The function return a subset of the sequences

Data files: 

[cleaned_data.mat](cleaned_data.mat) - sequences after filtering and cleaning

[s4.mat](s4.mat) - all prime numbers that exist in cleaned_data.mat 

