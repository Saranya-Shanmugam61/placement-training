def my_atoi():
    s = input("Enter a string: ").strip()
    sign = 1
    i = 0
    result = 0

    if not s:
        print("Converted integer: 0")
        return

    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1

    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    print(f"Converted integer: {max(-2**31, min(sign * result, 2**31 - 1))}")

my_atoi()
