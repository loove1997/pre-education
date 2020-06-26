"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요


예시
<입력>
첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력
두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력

<출력>
첫 번째(두 번째) 참가자의 승리입니다. or 비겼습니다.

"""

import random

print('<입력>')
print('첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ', end=' ')
text = input()
#여기서 엔터를 쳐도 콘솔에 줄바꿈이 안되는 방법은 없을까? --> 불가능..?
#python3에서는 raw_input()이 없어졌다.
if text == '':
    rand1 = random.randrange(1, 6, 1)
    print(rand1)

print('두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ', end=' ')
text = input()
if text == '':
    rand2 = random.randrange(1, 6, 1)
    print(rand2)

print('<출력>')

if rand1 > rand2:
    print('첫 번째 참가자의 승리입니다.')
elif rand1 < rand2:
    print('두 번째 참가자의 승리입니다.')
else:
    print('비겼습니다.')