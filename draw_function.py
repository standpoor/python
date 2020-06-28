import matplotlib.pyplot as plt

start = -5
end = 5


def func1(x):
    return x*x


def func2(x):
    return 4 * pow(x, 3) - 3


def func3(x):
    return 5* pow(x, 4) -5


def func4(x):
    return pow(2, x)



input = []
step = (end - start) / 10000
for index in range(10001):
    input.append(start + step * index)

output1 = []
output2 = []
output3 = []
output4 = []
for x in input:
    output1.append(func1(x))
    output2.append(func2(x))
    output3.append(func3(x))
    output4.append(func4(x))



x_ticks= [-5, -4.5, -4, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2.0, 2.5, 3.0, 3.5, 4, 4.5, 5]

plt.xticks(x_ticks)

plt.ylim(-20, 20)

plt.title("Polynomial display") # title
plt.ylabel("Polynomial output") # y label
plt.xlabel("Polynomial input") # x label
plt.plot(input, output1, label="x**")
plt.plot(input, output2, label="x***")
plt.plot(input, output3, label="x****")
plt.plot(input, output4, label="2**x")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
