f = open('number.txt')

text = []
for line in f:
    text.append(line)

f.close()

print(text)

total = 0
for number in text:
    total += int(number.strip(", \n"))

print("The average number is:{0}".format( total/len(text)))