# team,wins,loss,draws,scored,conceded
# Manchester United,30,3,5,88,20/Arsenal,24,6,8,98,29/Chelsea,22,8,8,98,29
class dic:
    def __init__(self,team,w,l,d,s,c):
        self.team = team
        self.point = 3*w + 0*l + 1*d
        self.gd = s-c 
        
    def __str__(self):
        return "['"+str(self.team)+"', {'points': "+str(self.point)+"}, {'gd': "+str(self.gd)+"}]"

def sortTeam(team):
    for i in range(len(team)-1,0,-1):
        for j in range(i):
            if team[j].point < team[j+1].point:
                team[j], team[j+1] = team[j+1], team[j]
            elif team[j].point == team[j+1].point:
                if team[j].gd < team[j+1].gd:
                    team[j], team[j+1] = team[j+1], team[j]
    return team

inp = [str(e).split(',') for e in input('Enter Input : ').split('/')]
lst = [dic(e[0],int(e[1]),int(e[2]),int(e[3]),int(e[4]),int(e[5])) for e in inp]

print('== results ==')
for i in sortTeam(lst):
    print(str(i))