"""
Manual Solution to calculate Combinations and Permutations

Task: You draw 2 cards from a standard 52-card deck without replacing
them. What is the probability that both cards are of the same suit?

Choices:
a. 1/156
b. 12/39
c. 1/39
d. 12/51 -- Answer

Solution:
♥️ = A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K = 13
♦️ = A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K = 13
♠️ = A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K = 13
♣️ = A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K = 13
Total: 52

S = {HH, DD, SS, CC, HD, HS, HC, DH, DS, DC, SH, SD, SC, CH, CD, CS}

Event A -> HH
- P(A) = P(H) * P(H) = 13/52 * 12/51 = 1/17

Event B -> DD
- P(B) = P(D) * P(D) = 13/52 * 12/51 = 1/17

Event C -> SS
- P(C) = P(S) * P(S) = 13/52 * 12/51 = 1/17

Event D -> CC
- P(D) = P(C) * P(C) = 13/52 * 12/51 = 1/17

Event: both have the same suit
P(A ∩ B ∩ C ∩ D) = P(A) + P(B) + P(C) + P(D) = P(HH) + P(DD) + P(SS) + P(CC) = 1/17 + 1/17 + 1/17 + 1/17 = 4/17
"""
