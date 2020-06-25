result = 200

while result > 100:
    result = int(input("Please input a number:"))


print(f"The input nubmer is {result}")

for index in range(100):
    if index % 2 == 0:
        continue
    elif index % 3 == 0:
        print(index)
    elif index % 29 == 0:
        break
    else:
        pass
