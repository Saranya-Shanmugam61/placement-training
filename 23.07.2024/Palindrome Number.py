def is_palindrome():
    x = int(input("Enter an integer: "))
    if x < 0:
        print(f"{x} is not a palindrome")
        return
    
    original = x
    reversed_x = 0
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10

    print(f"{original} is {'a palindrome' if original == reversed_x else 'not a palindrome'}")

is_palindrome()
