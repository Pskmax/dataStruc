print('*** Converting hh.mm.ss to seconds ***')
hh,mm,ss = input('Enter hh mm ss : ').split()
hh = int(hh)
mm = int(mm)
ss = int(ss)
output = (hh*60*60) + (mm*60) + ss
print(hh + ':' + mm +':' + ss, '=', '{:,}'.format(output), 'seconds')
