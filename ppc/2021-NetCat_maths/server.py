#!/usr/bin/python3
from time import time
from random import randint, choice


def fail():
    print("You are a looser")
    exit(0)


operations_d = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b}
operations = list(operations_d.items())


ITERATIONS_NUM = 100
OPERANDS_LIMIT = 1000
TIMEOUT_SEC = 2.


if __name__ == "__main__":
    print("Hello! Try to calculate", ITERATIONS_NUM, "expressions. You have only 2 seconds!")

    for i in range(ITERATIONS_NUM):
        a = randint(1, OPERANDS_LIMIT)
        b = randint(1, OPERANDS_LIMIT)
        op, func = choice(operations)

        print(f"Try {a} {op} {b}")

        start = time()
        ans = input("")

        if time() - start > TIMEOUT_SEC:
            fail()

        try:
            ans = int(ans)
        except ValueError:
            fail()

        if ans != func(a, b):
            fail()

        print("Good job!")

    print("Wow, you are really cool. Here is your flag: CTF{t1m3_t0_dr4w_4_h34rt}")
