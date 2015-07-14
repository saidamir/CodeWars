def Descending_Order(num):
    return int(''.join(sorted(str(num), reverse=True)))

assert Descending_Order(0) == 0
assert Descending_Order(15) == 51
assert Descending_Order(123456789) == 987654321