import math


def cal_sd(x):
    y = len(x)
    sum_of_powered_x_minus_x_bar = 0
    for n in range(0, len(x)):
        this_x = int(x[n])
        x_bar = sum(x) / len(x)
        power_of_x_minus_x_bar = (this_x - x_bar) ** 2
        sum_of_powered_x_minus_x_bar += power_of_x_minus_x_bar
    v = sum_of_powered_x_minus_x_bar / (y - 1)
    answer = math.sqrt(v)
    return answer
