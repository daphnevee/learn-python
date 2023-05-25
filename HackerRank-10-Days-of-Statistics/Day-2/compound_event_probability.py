"""
Manual Solution to calculate Compound Event Probability

Task: There are 3 urns labeled X, Y, and Z.
- Urn X contains 4 red balls and 3 black balls.
- Urn Y contains 5 red balls and 4 black balls.
- Urn Z contains 4 red balls and 4 black balls.
One ball is drawn from each of the 3 urns. What is the probability that,
of the 3 balls drawn, 2 are red and 1 is black?

Choices:
a. 10/63
b. 17/42 -- Answer
c. 2/7
d. 31/126

Solution:
Urn X
- Red: 4
- Black: 3
- Total: 7

Urn Y
- Red: 5
- Black: 4
- Total: 9

Urn Z:
- Red: 4
- Black: 4
- Total: 8

Event A: Urn X -> Red, Urn Y -> Red, Urn Z -> Black
Event B: Urn X -> Red, Urn Y -> Black, Urn Z -> Red
Event C: Urn X -> Black, Urn Y -> Red, Urn Z -> Red

Event A: P(R, R, B) = P(R) * P(R) * P(B) = (4/7) * (5/9) * (1/2) = 20/126
Event B: P(R, B, R) = P(R) * P(B) * P(R) = (4/7) * (4/9) * (1/2) = 16/126
Event C: P(B, R, R) = P(B) * P(R) * P(R) = (3/7) * (5/9) * (1/2) = 15/126

P(2 reds, 1 black) = P(R, R, B) + P(R, B, R) + P(B, R, R) = 20/126 + 16/126 + 15/126 = 51/126 = 17/42
"""
