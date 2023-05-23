"""
Manual Solution to calculate Basic Probability

Task: In a single toss of 2 fair (evenly-weighted) six-sided dice,
find the probability that their sum will be at most 9.

Choices:
a. <p>2/3</p>
b. <p>5/6</p> -- Answer
c. <p>1/4</p>
d. <p>1/6</p>

Solution:
> Experiment: rolling 2 fair (evenly-weighted) 6-sided dice
> Sample space (S): S = {(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2, 1), (2, 2), (2, 3), (2, 4), 
                         (2, 5), (2, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), 
                         (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), 
                         (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6) = 6 x 6 = 36
> Event(A): that the sum of the 2 rolled dice is 9
    Case 1: Sum >= 10 -> (4, 6), (5, 5), (5, 6), (6, 4), (6, 5), (6, 6)
        - P(Sum >= 10) = 6/36 = 1/6
    Case 2: Sum <= 9
        - P(Sum <= 9) = 1 - P(Sum >= 10) = 1 - 1/6 = 5/6
"""
