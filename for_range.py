
for row in range(1, 10):
    for column in range(1, 10):
        print(row * column)


for row in range(1, 10):
    result = ""
    for column in range(1, 10):
        result = result + str(row * column)
    print(result)