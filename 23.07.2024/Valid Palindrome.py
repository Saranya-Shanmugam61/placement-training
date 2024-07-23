def valid_palindrome():
    s = input("Enter a string: ").lower()
    filtered_s = ''.join(c for c in s if c.isalnum())
    print(f"'{s}' is {'a palindrome' if filtered_s == filtered_s[::-1] else 'not a palindrome'}")

valid_palindrome()
