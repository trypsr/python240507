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



# value = 5
# while value > 0:
#     print(value)
#     value -=1

# lst = [100, "apple", 3.14]
# for item in lst :
#     print(item)

# fruits = {"apple":100, "kiwi":200}
# for k,v in fruits.items():
#     print(k,v)

# print("---range()함수---")
# print(list(range(10)))
# print(list(range(1,32)))

print("---list 함축---")
lst = list(range(1, 11))
print(lst)
print([i**2 for i in lst if i>5])
d = {100:"apple",200:"kiwi"}
print([v.upper() for v in d.values()])

print("--필터링--")
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

#함수를 정의
def getBiggerThan20(i):
    return i>20
print("--필터링한 경우--")
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("--람다함수를 사용--")
iterL = filter(lambda x:x<20, lst)
for item in iterL:
    print(item)