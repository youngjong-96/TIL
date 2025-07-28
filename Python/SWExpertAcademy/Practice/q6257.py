#리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다.

fruit = ['   apple    ','banana','  melon']

new_fruit = [i.strip() for i in fruit]

result = {}

for fruit in new_fruit:
    result[fruit] = len(fruit)

print(result)