import matplotlib.pyplot as plt

def func1(x):
    return 10*x*x + 3*x + 5

def func2(x):
    return pow(x, 3) - 3

def func3(x):
    return pow(x, 4) -5


input = []
step = (5 - (-5)) / 1000
for index in range(1001):
    input.append(-5 + step * index)

output1 = []
output2 = []
output3 = []
for x in input:
    output1.append(func1(x))
    output2.append(func2(x))
    output3.append(func3(x))

plt.title("Polynomial display") # title
plt.ylabel("Polynomial output") # y label
plt.xlabel("Polynomial input") # x label
plt.plot(input, output1, label="x**")
plt.plot(input, output2, label="x***")
plt.plot(input, output3, label="x****")
plt.legend(loc='upper right')
plt.show()
