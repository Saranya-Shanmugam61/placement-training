def reverse_integer():
    x = int(input("Enter an integer: "))
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_x = int(str(x)[::-1])
    
    if reversed_x > 2**31 - 1:
        print("Reversed integer is out of bounds!")
    else:
        print(f"Reversed integer is: {sign * reversed_x}")

reverse_integer()
