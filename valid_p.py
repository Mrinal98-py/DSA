def isPalindrome(s):
    s1 = ''
    for i in s:
        if i.isalnum():
            s1 = s1 + i
            low_str = s1.lower()
        
    print(low_str)
    if low_str == low_str[::-1]:
        print("T")
    else:
        print("F")

s = "A man, a plan, a canal: Panama"
isPalindrome(s)