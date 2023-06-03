def isPalindrome(value):
    if isinstance(value, str):
        string = value.replace(" ", "").lower()
        t = len(string)
        palindrome = ''
        for i in range(t-1, -1, -1):
            palindrome += string[i]
        if string == palindrome:
            return True
        else:
            return False
    else: # For integer and float/double values
        value = str(value)
        t = len(value)
        palindrome = ''
        for i in range(t-1, -1, -1):
            palindrome += value[i]
        if value == palindrome:
            return True
        else:
            return False
