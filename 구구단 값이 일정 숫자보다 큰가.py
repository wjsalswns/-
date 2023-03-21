a = int(input('숫자를 입력하세요 >> '))
b = int(input())
print(f'{b}보다 큰가?')
for k in range(1, 10):
    print(f'{a} * {k} = {a * k}')
    if a * k > b:
        print(f'{b}보다 크네')
    elif a * k < b:
        print(f'{b}보다 작네')
    elif a * k == b:
        print(f'{b}이랑 같네')