#CSCI 1133 - Fall 2019 HW 5 (Testing Code)
from moha0469_5A import RPSai #Switch sjguy000_5A to your file's name
#Plays opponent's last move twice in a row

def winner(p1,p2):
    if p1+p2 in ["RS","SP","PR"]:
        return 1
    if p1==p2:
        return 0
    else:
        return -1

comp = RPSai()
wins = 0
games = 0
myLastmove = "R"
oppLastmove = "R"
playcount = 0
while games < 300:
    move = myLastmove
    if playcount == 0:
        move = oppLastmove
        playcount = 2
    playcount -= 1
    cpuMove = comp.playMovePro()
    comp.opponentMove(move)
    oppLastmove = cpuMove
    myLastmove = move
    w = winner(cpuMove,move)
    #print(cpuMove, move, w)
    if w == 1: #we win
        wins += 1
    if w == 0: #tie
        wins += .5

    games += 1

print("Win rate: %.3f"%(wins/games)) 
