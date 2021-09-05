n,p,vote = int(input('*** Election ***'+'\nEnter a number of voter(s) : ')),input().split(' '),[]
for i in p:
    if(int(i) > 0 and int(i) <=20) :
        vote.append(int(i))

if len(vote)<1 :
     print('*** No Candidate Wins ***')
elif len(vote)>0:
    print((max(vote,key=vote.count)))