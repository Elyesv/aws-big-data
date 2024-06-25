import time

def handler():

    with open('texte.txt', 'r') as file:
        text = file.read().replace('\n', '').replace('.', '').replace(',','').lower()
        list_words = text.split(' ')
    
        # len_list_words = len(list_words)
        # print('Number of words in the text: ', len_list_words)
                    
        # start_time = time.time()
        # index = linear_search(list_words, 'suspendisse')
        # end_time = time.time()
        # print('The word is found at index: ', index)
        # print('Execution time to find the element with linear search: ', end_time - start_time, 'seconds')

                
        # occurence = count_linear(list_words, 'suspendisse')
        # print('The word is found ', occurence, ' times')
        
        start_time = time.time()
        sorted_list = sorted(list_words)
        end_time = time.time()
        print('Execution time to sort the list: ', end_time - start_time, 'seconds')
        start_time = time.time()
        index = binary_search_iterative(sorted_list, 'suspendisse')
        end_time = time.time()
        print('The word is found at index: ', index)
        print('Execution time of binary search (iterative version): ', end_time - start_time, 'seconds')
        
        start_time = time.time()
        index = binary_search_recursive(sorted_list, 'suspendisse')
        end_time = time.time()
        print('The word is found at index: ', index)
        print('Execution time of binary search (recursive version): ', end_time - start_time, 'seconds')

            
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

def binary_search_iterative(sorted_list, word):
        low = 0
        high = len(sorted_list) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = sorted_list[mid]
            if guess == word:
                return mid
            if guess > word:
                for i in range(mid, low, -1):
                    if sorted_list[i] == guess:
                        high = mid - 1
            else:
                for i in range(mid, high):
                    if sorted_list[i] == guess:
                        low = mid + 1
        return None
    
def binary_search_recursive(sorted_list, word):
    if len(sorted_list) == 0:
        return None
    mid = len(sorted_list) // 2
    guess = sorted_list[mid]
    if guess == word:
        return mid
    if guess > word:
        return binary_search_recursive(sorted_list[:mid], word)
    else:
        result = binary_search_recursive(sorted_list[mid+1:], word)
        if result is not None:
            return result + mid + 1
    return None



class Complexite:
    def __init__(self):
        self.memo = {}
    
    def fibonacci_recursive(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci_recursive(n-1) + self.fibonacci_recursive(n-2)

    def fibonacci_memo(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = self.fibonacci_memo(n-1) + self.fibonacci_memo(n-2)
        self.memo[n] = result
        return result


def main():
    handler()
    
    c = Complexite()

    # start_time = time.time()
    # fibo = c.fibonacci_recursive(35)
    # end_time = time.time()
    # print('Fibonacci result: ', fibo)
    # print('Execution time of fibonacci_recursive: ', end_time - start_time, 'seconds')

    # start_time = time.time()
    # fibo_memo = c.fibonacci_memo(50)
    # end_time = time.time()
    # print('Fibonacci result with memoization: ', fibo_memo)
    # print('Execution time of fibonacci_memo: ', end_time - start_time, 'seconds')
    
if __name__ == "__main__":
    main()