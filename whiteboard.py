# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') -> igPay atinlay siay oolcay
# pig_it('Hello world !')    -> elloHay orldway !

def solution(string): #O(n2)
    str_arr = string.split(" ") # O(n)
    empty_lst = []
    
    for word in str_arr: # O(n)
        if not word.isalpha(): # O(1)
            empty_lst.append(word) # O(1)
            continue
        empty_lst.append(f"{word[1:]}{word[0]}ay") # O(n)

    return ' '.join(empty_lst) #O(n)


def solution(sentence):
    words = sentence.split(' ')
    new_words = []

    for word in words:
        if word.isalpha():
            moved = word[1:] + word[0] + 'ay'
            new_words.append(moved)
        else:
            new_words.append(word)

    result = ' '.join(new_words)
    return result

    def solution(string):
    return ' '.join([f"{word[1:]}{word[0]}ay" if len(word) >= 2 else word for word in string.split(" ")])