"""19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']


예시
<입력>
print(list)

<출력>
['charlie', 'foxtrot']

 """

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']

list = []

for word in a:
    num = 0

    for i in word:
        #단어 철자마다 알파벳일경우 num++
        if ord('a') <= ord(i.lower()) <= ord('z'):
            num = num + 1
    #알파벳이 총7개면 list에 추가
    if num == 7:
        list.append(word)

print('<출력>')
print(list)