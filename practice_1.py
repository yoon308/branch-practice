num = int(input('년도 입력: '))

if ((num%4 == 0) and (num%100 != 0)) or ( num%400 == 0):
    print('윤년')
else:
    print('평년') 
