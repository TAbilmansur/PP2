def palindrome(a):
    return a == a[::-1]
a = input()
print(palindrome(a))