#CSCI 1133 - Fall 2019 HW 5 (Testing Code)
from moha0469_5A import RPSai #Switch sjguy000_5A to your file's name
#??? (A Super Secret test case :) -- it's pretty good for how short it is!)

def winner(p1,p2):
    if p1+p2 in ["RS","SP","PR"]:
        return 1
    if p1==p2:
        return 0
    else:
        return -1

comp = RPSai()

w = 0; g = 0; l = "R"
while g < 300:
    m = "RPS"["SRP".find(l)]
    c = comp.playMovePro()
    comp.opponentMove(m)
    l = c
    r = winner(c,m)
    if r>-1: w += r/2+.5
    g += 1

print("Win rate: %.3f"%(w/g)) 
