def box(items,number_of_box):
    left = max(items)
    right = sum(items)
    while left <= right:
        box_size = (left+right)//2
        box_count = 0
        i = 0
        while i < len(items):
            weight = 0
            while i < len(items) and weight + items[i] <= box_size:
                weight += items[i]
                i += 1
            box_count += 1

        if box_count <= number_of_box:
            right = box_size - 1
        else:
            left = box_size + 1
    return left
    

left,right = input('Enter Input : ').split('/')
items = list(map(int,left.split()))
num = int(right)
print('Minimum weigth for',num,'box(es) =',box(items,num))