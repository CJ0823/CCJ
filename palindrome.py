def is_palindrome(word):
    syl = list(word)
    for i in range(0,int(len(syl)/2)):
        left = syl[i]
        right = syl[-1-i]
        if left != right:
            return False
    return True
print(is_palindrome("raceca"))