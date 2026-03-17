def reverse(wordy):
    length = len(wordy)
    global message
    x = wordy
    message = ""
    for i in range (length):
        y = x[-1:]
        message += y
        x = x[:-1]
    return(message)

def check_palindrome(word):
    word = word.lower()
    amount_letters = len(word)
    if amount_letters == 1:
        global palindrome
        palindrome = True
        return True
    elif amount_letters % 2 == 0:
        letters = amount_letters // 2
        word_p1 = word[0:letters]
        word_p2 = word[letters:amount_letters]
        a = reverse(word_p2)
        if word_p1 == a :
            palindrome = True
            return True
        else :
            palindrome = False
            return False
    elif amount_letters % 2 == 1:
        letters = (amount_letters - 1) // 2
        word_p1 = word[0:letters]
        word_p2 = word[letters + 1:amount_letters]
        a = reverse(word_p2)
        if word_p1 == a :
            palindrome = True
            return True
        else :
            palindrome = False
            return False
        
check_palindrome("tacocat")
if palindrome == True :
    print (True)
elif palindrome == False :
    print (False)