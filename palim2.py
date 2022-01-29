# Check if a string is a palindrome
def check_palindrome(s):
    s = list(s)
    lent = len(s)
    start = 0; end = lent - 1;
    while(start < end):
        print(start, end)
        if end > start:
            if (s[start] == s[end]):
                start+=1
                end-=1
            else:
                print("String is not palindrome")
                return;
        else:
            break
    print("String is Palindrome")
    return

check_palindrome("ddssdd")