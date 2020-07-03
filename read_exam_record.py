f = open('exam_record')

text = []
for line in f:
    text.append(line)

f.close()

for line in text:
    print(line.split())