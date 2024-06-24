def handler():
    with open('texte.txt', 'r') as file:
        text = file.read().replace('\n', '').replace('.', '').replace(',','').lower()
        list_words = text.split(' ')
        
        # len_list_words = len(list_words)
        # print('Number of words in the text: ', len_list_words)
            
        # index = linear_search(list_words, 'est')
        # print('The word is found at index: ', index)
        
        # occurence = count_linear(list_words, 'suspendisse')
        # print('The word is found ', occurence, ' times')
        
        

def linear_search(list_words, word):
    for i in range(len(list_words)):
        if list_words[i] == word:
            return i
    return -1

def count_linear(list_words, word):
    word_count = 0
    for w in list_words:
            if w == word:
                word_count += 1
    return word_count
    

def main():
    handler()
    
if __name__ == "__main__":
    main()