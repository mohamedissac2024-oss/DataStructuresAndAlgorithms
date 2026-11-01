# 5 -> 5+4+3+2+1
def up_to_n(n):
    # add all the values up to n
    total = 0
    for i in range(1, n + 1):
        print("I is", i, "Sum is", total)
        total = total + i
    print("Sum is", total)
    return total

up_to_n(5)
