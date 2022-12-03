
# opponent: A for Rock, B for Paper, and C for Scissors.
# player:  X for Rock, Y for Paper, and Z for Scissors

# score 1: 1 for Rock, 2 for Paper, and 3 for Scissors
# score 2: 0 if you lost, 3 if the round was a draw, and 6 if you won

stratguide = [ x.split(" ") for x in open('input').read().strip().split("\n") ]

# PART ONE
score = {}
# ties
score[('A','X')] = 4
score[('B','Y')] = 5
score[('C','Z')] = 6

# win
score[('A','Y')] = 8
score[('B','Z')] = 9
score[('C','X')] = 7

# loss
score[('A','Z')] = 3
score[('B','X')] = 1
score[('C','Y')] = 2


# res1
print('res1 not 14711')
print('res1 not  9911')
print('res1', sum( score[tuple(x)] for x in stratguide ))

# PART TWO
# opponent: A for Rock, B for Paper, and C for Scissors.
# score 1: if I play: 1 for Rock, 2 for Paper, and 3 for Scissors
# actually X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
# score 2: 0 if you lost, 3 if the round was a draw, and 6 if you won
score2 = {}
score2[('A','X')] = 0 + 3
score2[('A','Y')] = 3 + 1
score2[('A','Z')] = 6 + 2

score2[('B','Y')] = 3 + 2
score2[('B','X')] = 0 + 1
score2[('B','Z')] = 6 + 3

score2[('C','X')] = 0 + 2
score2[('C','Y')] = 3 + 3
score2[('C','Z')] = 6 + 1


print('res2', sum( score2[tuple(x)] for x in stratguide ))
