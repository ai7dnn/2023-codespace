# 1. Hello, World! 출력하기
print("Hello, World!")

# 2. 변수 사용하기
# name = input("이름을 입력하세요: ")
name = '홍길동'
print("안녕하세요, " + name + "님!")

# 3. 숫자 계산하기
num1 = 10
num2 = 5
result = num1 + num2
print("결과:", result)

# 4. 조건문 사용하기
# age = int(input("나이를 입력하세요: "))
age = 30
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 5. 반복문 사용하기
for i in range(5):
    print("반복문 예제:", i)

# 6. 리스트 활용하기
fruits = ["사과", "바나나", "오렌지"]
print("과일 목록:", fruits)

# 7. 함수 정의하기
def square(x):
    return x * x
result = square(5)
print("결과:", result)

# 8. 파일 입출력
""" file_name = "example.txt"
with open(file_name, "w") as f:
    f.write("파일 입출력 예시")
"""

# 9. 모듈 사용하기
import random
random_number = random.randint(1, 100)
print("랜덤 숫자:", random_number)
try:
    x = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")