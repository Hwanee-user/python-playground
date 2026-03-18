# 2026-03-18 Day2 f-string, input

name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")

print("제 이름은 " + name + "이고, 나이는 " + age + "살 입니다.")
print(f"제 이름은 {name}이고, 저는 내년에 {int(age)+1}살이 됩니다.")

fruit = input("구매할 과일의 이름을 입력하세요: ")
price = 2000
count = int(input("구매할 과일의 개수를 입력하세요: "))

print(f"{fruit} {count}개는 {price*count}원입니다.")

