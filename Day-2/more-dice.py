"""
Manual Solution to calculate Basic Probability for More Dice

Task: In a single toss of 2 fair (evenly-weighted) six-sided dice,
find the probability that the values rolled by each die will be different
and the two dice have a sum of 6.

Choices:
a. 1/9 -- Answer
b. 1/6
c. 2/3
d. 5/6

Solution:
> Experiment: rolling 2 fair (evenly-weighted) 6-sided dice
> Sample space (S): S = {(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2, 1), (2, 2), (2, 3), (2, 4), 
                         (2, 5), (2, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), 
                         (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), 
                         (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6) = 6 x 6 = 36
> Event(A): that the values rolled by each die will be different and the two dice have a sum of 6
    -> (1, 5), (2, 4), (4, 2), (5, 1)
    - P(Diff values, Sum = 6) = 4/36 = 1/9
"""
