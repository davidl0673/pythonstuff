word1 = input("Enter a word: ").lower()
word2 = input('pick a second word').lower()

fixed = sorted(word1)
refixed = "".join(fixed)

fixed1 = sorted(word2)
refixed2 = "".join(fixed1)

if refixed == refixed2:
    print('these are anagrams ')

else:
       print('these are not anagrams')



