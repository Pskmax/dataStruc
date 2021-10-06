# BMI = น้ำหนักหน่วย (kg) / ( ความสูงหน่วย (m) * ความสูงหน่วย (m))

print(' *** BMI ***')
w,h = input('Enter your weight(kg) and height(m) : ').split()
w = int(w)
h = float(h)
bmi = w / (h**2)
print('Your status is : ',end='')
if bmi < 18.5:
    print('Below normal weight.')
elif bmi < 25:
    print('Normal weight.')
elif bmi < 30:
    print('Overweight.')
elif bmi < 35:
    print('Case I Obesity.')
elif bmi < 40:
    print('Case II Obesity.')
else:
    print('Case III Obesity.')