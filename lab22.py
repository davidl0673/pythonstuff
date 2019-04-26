
from string import punctuation

with open('tail.txt') as f:
    strip = f.read()
    translator = str.maketrans('', '' , punctuation)
    string_without_punct = strip.translate(translator)
    
    book_list = string_without_punct.split(' ')

number_of_words = (len(book_list))
number_letters = (len(strip))
sentaces = strip.count('.')
sentaces += strip.count('?')
sentaces += strip.count('!')
print(number_of_words)
print(number_letters)
print(sentaces)

ari1 = 4.71 * (number_letters / number_of_words) 
ari2 = ((number_of_words / sentaces) * .5) -23.43
ari_score = min(int(ari1 + ari2), 14) 
print(ari_score)
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}



print(f'Your ARI score is {ari_score}. This is suitable for {ari_scale[ari_score]["grade_level"]}')


