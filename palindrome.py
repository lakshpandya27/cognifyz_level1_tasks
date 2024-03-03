 
def isPalindrome(s):
    return s == s[::-1]

s = input("Enter a String:");
ans = isPalindrome(s)
 
if ans:
    print("Yes, it is Palindrome")
else:
    print("No, it ain't Palindrome")
