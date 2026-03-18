# 2026-03-18 Day2 f-string, input

# # sourcery skip: use-fstring-for-concatenation
# name = input("이름을 입력하세요: ")
# age = input("나이를 입력하세요: ")

# print("제 이름은 " + name + "이고, 나이는 " + age + "살 입니다.")
# print(f"제 이름은 {name}이고, 저는 내년에 {int(age)+1}살이 됩니다.")

# fruit = input("구매할 과일의 이름을 입력하세요: ")
# price = 2000
# count = int(input("구매할 과일의 개수를 입력하세요: "))

# print(f"{fruit} {count}개는 {price*count}원입니다.")

# food = "피자"
# price = 18000
# print(f"오늘 점심은 {food}, 가격은 {price}원입니다.")

# name = input("당신의 이름은?")
# age = input("당신의 나이는?")
# city = input("당신이 사는 도시는?")
# print(f"안녕하세요, 저는 {name}입니다. 저는 {age}살 이고 {city}에 살고 있습니다.")
# print()

# a = "100"
# b = "3.14"

# print(f"a={a}, b={b}이다.")
# print(f"int a는 {int(a)}이다.")
# print("int b는 실행되지 않는다.")
# print(f"float a는 {float(a)}이다.")
# print(f"float b는 {float(b)}이다.")
# print(f"int(float b)는 {int(float(b))}이다.")

# print(f"int a + int(float b)는 {int(a) + int(float(b))}이다.")
# print(f"float a + float b는 {float(a) + float(b)}이다.")

# print(f"str a + str b는 실제 연산이 이뤄지지 않습니다. 결과는 {a + b}입니다.")

name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
height = float(input("키를 입력하세요: "))

print("=== 신상 정보 ===")
print(f"이름: {name}")
print(f"나이: {age}")
print(f"키: {height}cm")
print(f"10년 후 나이 : {age + 10}살")
