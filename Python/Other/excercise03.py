print('*** Election ***')
num = input('Enter a number of voter(s) : ')
inp = input().split()
vote = []
for i in inp:
    if int(i) > 0 and int(i) <= 20:
        vote.append(i)
if len(inp) <= 0:
    print('*** No Candidate Wins ***')
else:
    print(max(vote,key=vote.count))
