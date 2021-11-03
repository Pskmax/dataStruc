def natural_sum(n,current = 1):
    if current == n:
        print(current,end=' ')
        return n
    print(current,'+',end=' ')
    return current + natural_sum(n,current+1)

print(' *** Natural sum ***')
num = int(input("Enter number : ")) 
print("= %.d" %(natural_sum(num)))