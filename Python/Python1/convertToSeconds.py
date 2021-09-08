print("*** Converting hh.mm.ss to seconds ***")
h,m,s = input("Enter hh mm ss : ").split()
h = int(h)
m = int(m)
s = int(s)
# check error case!

if m > 59 or m < 0:
    print("mm"+"("+str(m)+")"+" is invalid!")
elif s > 59 or s < 0:
    print("ss"+"("+str(s)+")"+" is invalid!")
else:
    ans = h*60*60 + m*60 + s
    if h<10:
        h="0"+str(h)
    if m<10:
        m="0"+str(m)
    if s<10:
        s="0"+str(s)
    h = str(h)
    m = str(m)
    s = str(s)
    ans = '{:,.0f}'.format(ans)
    ans = str(ans)
    # output
    print(h + ":" + m + ":" + s + " = " + ans + " seconds")