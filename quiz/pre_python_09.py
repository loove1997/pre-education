"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F

예시
<입력>
score : 88

<출력>
A

"""

print('<입력>')
scr = input('score : ')

print('<출력>')

if int(scr) < 21:
    grade = 'F'
elif int(scr) < 41:
    grade = 'D'
elif int(scr) < 61:
    grade = 'C'
elif int(scr) < 81:
    grade = 'B'
else:
    grade = 'A'

print(grade)