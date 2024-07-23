def longest_substring_without_repeating():
    s = input("Enter a string: ")
    chars = set()
    left = 0
    result = 0

    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        result = max(result, right - left + 1)

    print(f"Length of longest substring without repeating characters: {result}")

longest_substring_without_repeating()
