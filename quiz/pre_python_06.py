"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★

예시
<입력>
숫자를 입력하세요 : 5

<출력>
    ★ 4,1
   ★★ 3,2
  ★★★ 2,3
 ★★★★ 1,4
★★★★★ 0,5 --> 1번째 for
 ★★★★
  ★★★
   ★★
    ★ --> 2번째 for


"""

print('<입력>')
num = input('숫자를 입력하세요 : ')

print('<출력>')

for i in range(int(num)): #num번째 줄 까지

    for spc in range(int(num)-(i+1)):
        print(' ', end='')

    for star in range(i+1):
        print('★', end='')

    print('');

for i in range(int(num)-1): #num+1번째 줄부터 끝까지

    for spc in range(i+1):
        print(' ', end='')

    for star in range(int(num)-(i+1)):
        print('★', end='')

    print('');