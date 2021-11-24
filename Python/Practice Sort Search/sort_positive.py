def sort_positive(lst):
    n = len(lst)
    for i in range(n-1,0,-1):
        change = False
        for j in range(i):
            if lst[j] > lst[j+1] and lst[j+1] >= 0:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                change = True
            elif j < len(lst)-2 and lst[j] > lst[j+2] and lst[j+2] >= 0:
                # เช็คว่าขนาดไม่เกิน list, เช็คว่าตัวที่ 1 มากว่าตัวที่ 3 หรือไม่, เช็คตัวที่ 3 ไม่ใช่ติดลบ
                # ปล. ทำไม่ได้ทุกกรณี เพราะว่าใช้กรณีที่มีตัวลบไม่เกิน 1 ตัวคั่น
                lst[j],lst[j+2] = lst[j+2],lst[j]
                change = True
        if not change:
            break
inp = list(map(int,input('Enter Input : ').split()))
sort_positive(inp)
print(*inp)