#분기 반복 구분
#선택한 블럭 주석처리 : ctrl + /
# score = int(input("점수를 입력:"))

# if 90 <= score <=100 :
#     grade ="A"
# elif 80 <= score <90 :
#     grade ="B"
# elif 80 <= score <90 :
#     grade ="C"
# elif 80 <= score <90 :
#     grade ="D"
# else :
#     grade ="F"

# print("등급은 : " + grade)



value = 5
while value > 0:
    print(value)
    value -=1

lst = [100, "apple", 3.14]
for item in lst :
    print(item)

fruits = {"apple":100, "kiwi":200}
for k,v in fruits.items():
    print(k,v)

print("---range()함수---")
print(list(range(10)))
print(list(range(1,32)))