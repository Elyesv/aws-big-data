class Complexite:
    def handler():
        with open('texte.txt', 'r') as file:
            text = file.read().replace('\n', '').replace('.', '').replace(',','').lower()
            list_words = text.split(' ')
            return list_words
            
            
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
    
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

def main():
    c = Complexite()
    # list_words = c.handler()
    
    # len_list_words = len(list_words)
    # print('Number of words in the text: ', len_list_words)
                
    # index = c.linear_search(list_words, 'est')
    # print('The word is found at index: ', index)
            
    # occurence = c.count_linear(list_words, 'suspendisse')
    # print('The word is found ', occurence, ' times')
    
    fibo = c.fibonacci(50)
    print('Fibonacci result: ', fibo)
    
if __name__ == "__main__":
    main()