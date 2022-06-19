import math
import matplotlib.pyplot as plt


def run():
    samples_x = input("Input your X samples: \n").split()
    for n in range(0, len(samples_x)):
        samples_x[n] = int(samples_x[n])

    samples_y = input("Input your Y samples: \n").split()
    for n in range(0, len(samples_y)):
        samples_y[n] = int(samples_y[n])

    population = len(samples_x)
    a = find_a(samples_x, samples_y, population)
    b = find_b(samples_x, samples_y, population)
    plt.plot(samples_x, samples_y)
    plt.xlabel('sample_x - axis')
    plt.ylabel('sample_y - axis')
    plt.title('Samples of X and Y')
    plt.show()
    get_answer(samples_x, samples_y, a, b)


def find_b(x, y, n):
    sum_of_y = sum(y)
    sum_of_x = sum(x)
    powered_of_sum_x = sum_of_x ** 2

    sum_of_powered_x = 0
    for i in range(0, len(x)):
        this_x = int(x[i])
        powered_x_ = this_x ** 2
        sum_of_powered_x += powered_x_

    sum_of_xy = 0
    for j in range(0, len(x)):
        this_x = int(x[j])
        this_y = int(y[j])
        multiple = this_x * this_y
        sum_of_xy += multiple

    # Simple Linear
    a0 = ((n * sum_of_xy) - (sum_of_x * sum_of_y)) / len(x)
    a1 = ((n * sum_of_powered_x) - powered_of_sum_x) / len(x)
    a2 = a0 / a1
    print(f"Sum of squares (SSx) : {a1}")
    print(f"Sum of products (SP) : {a0}")
    return a2

    # Regression Analysis
    # a0 = (sum_of_y * sum_of_powered_x) - (sum_of_x * sum_of_xy)
    # a1 = (n * sum_of_powered_x) - powered_of_sum_x
    # a2 = a0 / a1


def find_a(x, y, n):
    sum_of_y = sum(y)
    sum_of_x = sum(x)
    powered_of_sum_x = sum_of_x ** 2

    sum_of_powered_x = 0
    for i in range(0, len(x)):
        this_x = int(x[i])
        powered_x_ = this_x ** 2
        sum_of_powered_x += powered_x_

    sum_of_xy = 0
    for j in range(0, len(x)):
        this_x = int(x[j])
        this_y = int(y[j])
        multiple = this_x * this_y
        sum_of_xy += multiple

    # Simple Linear
    b0 = (sum_of_x * sum_of_xy) - (sum_of_y * sum_of_powered_x)
    b1 = powered_of_sum_x - (n * sum_of_powered_x)
    b2 = b0 / b1
    return b2

    # Regression Analysis
    # b0 = (n * sum_of_xy) - (sum_of_x * sum_of_y)
    # b1 = (n * sum_of_powered_x_) - sum_of_powered_x_
    # b2 = b0 / b1


def sd_cal(x):
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


def find_r_by_a(sx, sy, a):
    r = (sx / sy) * a
    return r


def find_r(x, y, sx, sy):
    sum_of_y = sum(y)
    sum_of_x = sum(x)
    p = len(x)

    sum_of_xy = 0
    for n in range(0, len(x), len(y)):
        if n in range(0, len(x)) == range(0, len(y)):
            multiple = x[n] * y[n]
            sum_of_xy += multiple

    r0 = sum_of_xy - (1 / p) * (sum_of_x * sum_of_y)
    r1 = (p - 1) * (sx * sy)
    r2 = r0 / r1
    return r2


def find_y(a, b, x):
    x = int(x)
    y = a + (b * x)
    return y


def find_x(a, b, y):
    y = int(y)
    x = (y - a) / b
    return x


def x_int_exception(x):
    try:
        val = int(x)
        return val
    except ValueError:
        try:
            val = float(x)
            return val
        except ValueError:
            return 0


def y_int_exception(y):
    try:
        val = int(y)
        return val
    except ValueError:
        try:
            val = float(y)
            return val
        except ValueError:
            return 0


def get_answer(samples_x, samples_y, a, b):
    x = input("Do you know 'X'? (if not, put 'n'):\n")
    y = input("Do you know 'Y'? (if not, put 'n'):\n")
    sx = float(sd_cal(samples_x))
    sy = float(sd_cal(samples_y))
    if x_int_exception(x) == 0 and y_int_exception(y) != 0:
        this_x = find_x(a, b, y)
        r = find_r(samples_x, samples_y, sx, sy)
        print(f" R = {r}")
        print("As the formula : x = (y - a) / b")
        print(f"Since you found Y = {y} , b = {b} , a = {a}\n"
              f"Then the calculation would be : x = ({y} - {a}) / {b}")
        print(f"Therefore, your X is  {this_x} ")
        samples_x.append(this_x)
        samples_y.append(x_int_exception(y))
        make_next_graph(samples_x, samples_y)

    elif x_int_exception(x) != 0 and y_int_exception(y) == 0:
        this_y = find_y(a, b, x)
        r = find_r(samples_x, samples_y, sx, sy)
        print(f" R = {r}")
        print("As the formula : y = a  + bX")
        print(f"Since you found X = {x} , a = {a} , b = {b}\n"
              f"Then the calculation would be : y = {a} + ({b} * {x})")
        print(f"Therefore, your Y is  {this_y} ")
        samples_x.append(x_int_exception(x))
        samples_y.append(this_y)
        make_next_graph(samples_x, samples_y)

    elif x_int_exception(x) == 0 and y_int_exception(y) == 0:
        r_by_a = find_r_by_a(sum(samples_x), sum(samples_y), a)
        print(f" R = {r_by_a}")
        print("As the formula : y = a + (b * x)")
        print(f"Since you found a = {a} , b = {b}\n"
              f"Then the calculation would be : y = {a} + {b}X")


def make_next_graph(samples_x, samples_y):
    plt.plot(samples_x, samples_y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Samples of X and Y')
    plt.show()
