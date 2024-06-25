import time

def handler():

    with open('text.txt', 'r') as file:
        text = file.read().replace('\n', '').replace('.', '').replace(',','').lower()
        list_words = text.split(' ')
    
        # len_list_words = len(list_words)
        # print('Number of words in the text: ', len_list_words)
                    

        
        start_time = time.time()
        for _ in range(500):
            index = linear_search(list_words, 'suspendisse')
            occurence = count_linear(list_words, 'suspendisse')
            # print('The word is found at index: ', index, ' and occurs ', occurence, ' times')
        end_time = time.time()
        print('Average execution time to find the element with linear search: ', (end_time - start_time) , 'seconds')

        print('-' * 50)

        start_time = time.time()
        sorted_list = sorted(list_words)
        end_time = time.time()
        print('Average execution time to sort the list: ', (end_time - start_time), 'seconds')

        print('-' * 50)

        start_time = time.time()
        for _ in range(500):
            count, index = binary_search_iterative(sorted_list, 'suspendisse')
            # print('The word occurs ', count, ' times at index:' , key)
        end_time = time.time()
        print('Average execution time of binary search (iterative version): ', (end_time - start_time), 'seconds')

        print('-' * 50)

        start_time = time.time()
        for _ in range(500):
            count, index = binary_search_recursive(sorted_list, 'suspendisse')
            # print('The word occurs ', count, ' times at index:' , key)
        end_time = time.time()
        print('Average execution time of binary search (recursive version): ', (end_time - start_time), 'seconds')
        
        print('-' * 50)
        
        start_time = time.time()
        hashmap = create_hashmap(list_words)
        end_time = time.time()  
        print('Average execution time to create the hashmap: ', (end_time - start_time), 'seconds')
        
        print('-' * 50)
        
        start_time = time.time()
        for _ in range(500):
            count, key = search_word_in_hashmap(hashmap, 'suspendisse')
            # print('The word occurs ', count, ' times at index:' , key)
        end_time = time.time()
        print('Average execution time of hashmap search: ', (end_time - start_time), 'seconds')            
                    
        
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
    count = 0

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == word:
            i = mid
            while sorted_list[i] == word:
                count += 1
                i -= 1
            i = mid + 1
            while i < len(sorted_list) and sorted_list[i] == word:
                count += 1
                i += 1
            return (count, mid)
        if guess > word:
            high = mid - 1
        else:
            low = mid + 1
    return (count, None)

def binary_search_recursive(sorted_list, word):
    if len(sorted_list) == 0:
        return (0, None)
    mid = len(sorted_list) // 2
    guess = sorted_list[mid]
    if guess == word:
        count = 1
        i = mid - 1
        while i >= 0 and sorted_list[i] == word:
            count += 1
            i -= 1
        i = mid + 1
        while i < len(sorted_list) and sorted_list[i] == word:
            count += 1
            i += 1
        return (count, mid)
    if guess > word:
        return binary_search_recursive(sorted_list[:mid], word)
    else:
        result = binary_search_recursive(sorted_list[mid+1:], word)
        if result[0] > 0:
            return (result[0], result[1] + mid + 1)
    return (0, None)

def create_hashmap(list_words):
    hashmap = [None] * int((len(list_words)/10))
    for word in list_words:
        key = sum(ord(c) for c in word)
        if hashmap[key] is None:
            hashmap[key] = [word]
        else:
            hashmap[key].append(word)
    return hashmap

def search_word_in_hashmap(hashmap, word):
    key = sum(ord(c) for c in word)
    occurrences = 0
    if hashmap[key] is not None:
        for w in hashmap[key]:
            if w == word:
                occurrences += 1
    return occurrences, key


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