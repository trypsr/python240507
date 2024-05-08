# DemoFile.py

# 파일쓰기 (유니코드)
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일읽기 
f2 = open("demo.txt", "rt", encoding="utf-8")
result = f2.read()
print(result)
print("--readline()메소드---")
f2.seek(0)
print(f2.readline(), end="")
print(f2.readline(), end="")
print("--readlines()메소드---")
f2.seek(0)
print(f2.readlines())
f2.close()
