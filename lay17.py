def Palindrome_check(word):
        word = input( 'pick a name ').lower()
        if word == word[::-1]:
            print('yes')
        else:
            print('no')

Palindrome_check('david')