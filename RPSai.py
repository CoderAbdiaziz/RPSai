class RPSai:
    
    def __init__(self):
        self.history = []
        self.countr = 0
        self.counts = 0
        self.countp = 0
    
    def opponentMove(self,move):
        if move == 'R' or move == 'S' or move == 'P':
            self.history.append(move)
        else:
            print('ERROR')

    def beatMove(self):
        if self.move == 'R':
            return 'P'
        if self.move == 'S':
            return 'R'
        if self.move == 'P':
            return 'S'

    def predictMove(self):
        for i in self.history:
            if i == 'R':
                self.countr += 1
            elif i == 'S':
                self.counts += 1
            else:
                self.countp += 1
        if self.countr > self.counts and self.countr > self.countp:
            return 'R'
        elif self.counts > self.countr and self.counts > self.countp:
            return 'S'
        else:
            return 'P'

    def playMove(self):
        if len(self.history) > 0:
            if self.predictMove() == 'R':
                return 'P'
            if self.predictMove() == 'S':
                return 'R'
            if self.predictMove() == 'P':
                return 'S'
        else:
            return 'R'
    
    def playMovePro(self):
        #RRRR or SSSS or PPPP method
        if len(self.history) > 4:
            length = len(self.history)
            if self.countr == length:
                return 'P'
            if self.counts == length:
                return 'R'
            if self.countp == length:
                return 'S'
        #uses R or P or S twice before switching
        
        #RSRSRS method
        if len(self.history) > 3:
            if self.history[0] == 'R' and self.history[1] == 'S' and self.history[2] == 'R':
                if len(self.history)%2 == 0:
                    return 'P'
                else:
                    return 'R'
            #SPSPSP method
            if self.history[0] == 'S' and self.history[1] == 'P' and self.history[2] == 'S':
                if len(self.history)%2 == 0:
                    return 'R'
                else:
                    return 'S'
            #SRSRSR method
            if self.history[0] == 'S' and self.history[1] == 'R' and self.history[2] == 'S':
                if len(self.history)%2 == 0:
                    return 'R'
                else:
                    return 'P'
            #PSPSPS method
            if self.history[0] == 'P' and self.history[1] == 'S' and self.history[2] == 'P':
                if len(self.history)%2 == 0:
                    return 'S'
                else:
                    return 'R'
            #RPRPRP method
            if self.history[0] == 'R' and self.history[1] == 'P' and self.history[2] == 'R':
                if len(self.history)%2 == 0:
                    return 'P'
                else:
                    return 'S'
            #PRPRPR method
            if self.history[0] == 'P' and self.history[1] == 'R' and self.history[2] == 'P':
                if len(self.hisotry)%2 == 0:
                    return 'S'
                else:
                    return 'P'
            #RSPRSPRSP method
            if self.history[0] == 'R' and self.history[1] == 'S' and self.history[2] == 'P':
                if len(self.history)%3 == 0:
                    return 'P'
                elif len(self.history)%3 == 1:
                    return 'R'
                else:
                    return 'S'
                
            #SPRSPRSPR method
            if self.history[0] == 'S' and self.history[1] == 'P' and self.history[2] == 'R':
                if len(self.history)%3 == 0:
                    return 'R'
                elif len(self.history)%3 == 1:
                    return 'S'
                else:
                    return 'P'
                
            #PRSPRSPRS method
            if self.history[0] == 'P' and self.history[1] == 'R' and self.history[2] == 'S':
                if len(self.history)%3 == 0:
                    return 'S'
                elif len(self.history)%3 == 1:
                    return 'P'
                else:
                    return 'R'
            #uses R or P or S twice before switching
            if self.history[0] == self.history[1] and self.history[2] == self.history[3]:
                if len(self.history)%2 == 1:
                    self.move = self.history[-1]
                    return self.beatMove()
                else:
                    return self.playMove()
                    
        else:
            return self.playMove()
        
        return self.playMove()
