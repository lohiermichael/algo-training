def add_binary(a: str, b: str) -> str:
    if len(a) < len(b):
        a = (len(b) - len(a)) * '0' + a
    else:
        b = '0' * (len(a) - len(b)) + b
    carry = 0
    res = ""
    while a and b:
        s = int(a[-1]) + int(b[-1]) + carry
        if s == 0:
            carry = 0
            res = "0" + res
        elif s == 1:
            carry = 0
            res = "1" + res
        elif s == 2:
            carry = 1
            res = "0" + res
        elif s == 3:
            carry = 1
            res = "1" + res
        a = a[:-1]
        b = b[:-1]

    if carry == 1:
        res = '1' + res

    return res


if __name__ == "__main__":
    a = "111"
    b = "11"
    print(add_binary(a, b))