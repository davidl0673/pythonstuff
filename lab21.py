from string import punctuation

def check(most_used_words, values):
   if values in most_used_words:
       most_used_words[values] += 1
   else:
       most_used_words.update({values: 1})

with open('tail.txt') as f:
    strip = f.read()
    translator = str.maketrans('', '' , punctuation)
    string_without_punct = strip.translate(translator)
    
    book_list = string_without_punct.split(' ')
   
    most_used_words = {}
    word_dict = {}
    stopwords = [ 'the', 'and', 'of', 'i', '' , 'to', 'my', 'a', 'in', 'that']
    count = 0
    
    for i in range(len(book_list)):
        if i+1 < len(book_list):
            values = (book_list[i], book_list[i +1])
            if ''not in values:
                check(most_used_words, values)
    
    for word in string_without_punct.lower().split(' '):
        if word in stopwords:
            continue
        if word in word_dict:
            word_dict[word] += 1 
        else:
            word_dict.update({word: 1})  

words = list(most_used_words.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])
    




    
    
    
    


    

