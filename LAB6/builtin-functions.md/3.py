s = str(input())
s = s.lower()
s1 = ''.join(reversed(s))
if s == s1:
    print("It is palindrome")
else:
    print("It is not palindrome")