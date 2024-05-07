# DemoListTuple.py
# 주석

lista = [1, 3, 5]
print(lista)
print(type(lista))
lista.append(4)
print(lista)
lista.remove(3);
print(lista)

print("--TUPLE 형식--")
tp = (10,20,30)
print(len(tp))
print(type(tp))

print("--set형식--")
a = {1,2,3}
b = {3,4,5}

print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("------튜플형식사용----")
def calc(a, b):
    return a+b, a*b

args = (1, 2)

result = calc(*args)
print(result)

print("id: %s, name:%s" % ("dirtyi", "park"))

print("---형식을 변환---")
a = list((1,2,3))
print(type(a))
