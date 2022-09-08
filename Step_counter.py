# code to count the number of ways we can climb n steps with the ability to either climb the steps by moving either
# 1 step, 2 steps or 3 steps at a time


step_counter_map = {}


def step_counter(n):
    if step_counter_map.__contains__(n):
        return n

    if n == 0:
        return 1

    elif n < 0:
        return 0

    return_value = step_counter(n-1) + step_counter(n-2) + step_counter(n-3)
    step_counter_map[n] = return_value
    return return_value


if __name__ == '__main__':
    print(step_counter(5))
    print(step_counter(1001))