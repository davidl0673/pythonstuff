def Palindrome_check(word):
        word = input( 'pick a name ').lower()
        if word == word[::-1]:
            print('yes it is a palindrome')
        else:
            print('not a palindrome')

Palindrome_check('david')


