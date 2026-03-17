def check_palindrome(word):
    word = word.lower()
    amount_letters = len(word)
    if amount_letters == 1:
        return True
    elif amount_letters % 2 == 0:
        letters = amount_letters // 2
        word_p1 = word[0:letters]
        word_p2 = word[letters:amount_letters]
    elif amount_letters % 2 == 1:
        letters = (amount_letters - 1) // 2
        word_p1 = word[0:letters]
        word_p2 = word[letters + 1:amount_letters]

        print (word_p1)


check_palindrome("a")
