import matplotlib.pyplot as plt

def func1(x):
    return 10*x*x + 3*x + 5

def func2(x):
    return 4 * pow(x, 3) - 3

def func3(x):
    return 5* pow(x, 4) -5


input = []
step = (3 - (-3)) / 10000
for index in range(10001):
    input.append(-3 + step * index)

output1 = []
output2 = []
output3 = []
for x in input:
    output1.append(func1(x))
    output2.append(func2(x))
    output3.append(func3(x))

x_ticks= [-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2.0, 2.5, 3.0]

plt.xticks(x_ticks)

plt.ylim(-10, 10)

plt.title("Polynomial display") # title
plt.ylabel("Polynomial output") # y label
plt.xlabel("Polynomial input") # x label
plt.plot(input, output1, label="x**")
plt.plot(input, output2, label="x***")
plt.plot(input, output3, label="x****")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
