'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''
#Card클래스 다른 파일에서 가져오기
from quiz2_3 import Card

class Multi_card(Card):

    def __init__(self):
        super().__init__()
        print('카드가 발급 되었습니다.')

    def charge(self, price):
        self.balance = self.balance + price
        print('{}이 충전되었습니다.'.format(self.balance))

    def consume(self, price, place):
        saleForMart = '마트'
        saleForTraffic = '교통'
        saleForMovie = '영화관'
        # 영화관 할인
        if place == saleForMovie:
            price = int(price * 0.8)
        elif place == saleForTraffic or place == saleForMart:
            price = int(price * 0.9)
        # 잔액이 부족할 때
        if self.balance < price:
            print('잔액이 부족합니다.')
        else:
            print('{}에서 {}원 사용했습니다.'.format(place, price))
            self.balance = self.balance - price
#다른파일에서 이 파일을 import 할 때 밑부분 실행을 막기 위해서
if __name__ == '__main__':
    multi_card=Multi_card()
    multi_card.charge(20000)
    multi_card.consume(5000,'마트')
    multi_card.consume(10000,'영화관')
    multi_card.consume(2000,'교통')
    multi_card.print()
