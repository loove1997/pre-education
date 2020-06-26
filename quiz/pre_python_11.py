"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(num1,num2):

    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp

    return num1

print(gcd(12,6))