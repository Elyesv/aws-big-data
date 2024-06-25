import time
import random

def handler():

    with open('text_light.txt', 'r') as file:
        text = file.read().replace('\n', '').replace('.', '').replace(',','').lower()
        list_words = text.split(' ')
    
        # len_list_words = len(list_words)
        # print('Number of words in the text: ', len_list_words)
        
        # print('-' * 50)
        
        # start_time = time.time()
        # for _ in range(1):
        #     sorted_list = bubble_sort(list_words)
        #     # print(sorted_list)
        # end_time = time.time()
        # print('Average execution time to sort the list (bubble sort): ', (end_time - start_time), 'seconds')
        
        # print('-' * 50)
        
        # start_time = time.time()
        # for _ in range(1):
        #     sorted_list = insertion_sort(list_words)
        #     # print(sorted_list)
        # end_time = time.time()
        # print('Average execution time to sort the list (insertion sort): ', (end_time - start_time), 'seconds')
        
        # print('-' * 50)
        
        # start_time = time.time()
        # for _ in range(1):
        #     sorted_list = save_sort(list_words)
        #     # print(sorted_list)
        # end_time = time.time()
        # print('Average execution time to sort the list (save sort): ', (end_time - start_time), 'seconds')
        
        # print('-' * 50)

        # start_time = time.time()
        # for _ in range(50):
        #     sorted_list = shell_sort(list_words)
        #     # print(sorted_list)
        # end_time = time.time()
        # print('Average execution time to sort the list (shell sort): ', (end_time - start_time), 'seconds')
        
        # print('-' * 50)
        
        # start_time = time.time()
        # for _ in range(50):
        #     sorted_list = quick_sort(list_words)
        #     # print(sorted_list)
        # end_time = time.time()
        # print('Average execution time to sort the list (quick sort): ', (end_time - start_time), 'seconds')
        
        # print('-' * 50)
        
        # start_time = time.time()
        # set = generate_set()
        # # print('The set is: ', set)
        # for _ in range(1000):
        #     pair, product = max_product_Ne2(set)
        # end_time = time.time()
        # print('The pair is: ', pair, ' and the product is: ', product)
        # print('Average execution time to find the pair with the maximum product: ', (end_time - start_time), 'seconds')
        
        # print('-' * 50)
        
        # start_time = time.time()
        # # print('The set is: ', set)
        # for _ in range(1000):
        #     pair, product = max_product_NlogN(set)
        # end_time = time.time()
        # print('The pair is: ', pair, ' and the product is: ', product)
        # print('Average execution time to find the pair with the maximum product: ', (end_time - start_time), 'seconds')
        
        # print('-' * 50)
        
        # start_time = time.time()
        # # print('The set is: ', set)
        # for _ in range(1000):
        #     pair, product = max_product_N(set)
        # end_time = time.time()
        # print('The pair is: ', pair, ' and the product is: ', product)
        # print('Average execution time to find the pair with the maximum product: ', (end_time - start_time), 'seconds')
        
        print('-' * 50)
        
        result = recursive_multiply(5, 3)
        print('The result of the multiplication is: ', result)
        
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr            
        
def insertion_sort(arr):
    sorted_arr = []
    while arr:
        min_val = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
        sorted_arr.append(min_val)
        arr.remove(min_val)
    return sorted_arr

def save_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for word in arr:
        if word < pivot:
            left.append(word)
        elif word == pivot:
            middle.append(word)
        else:
            right.append(word)
    return quick_sort(left) + middle + quick_sort(right)

def generate_set():
    positive_numbers = set(random.sample(range(1, 1000), 300))
    negative_numbers = set(-i for i in random.sample(range(1, 1000), 300))
    return positive_numbers.union(negative_numbers)

def max_product_Ne2(numbers):
    max_product = float('-inf')
    max_pair = None

    for i in numbers:
        for j in numbers:
            if i != j:
                product = i * j
                if product > max_product:
                    max_product = product
                    max_pair = (i, j)

    return max_pair, max_product

def max_product_NlogN(numbers):
    numbers = quick_sort(list(map(lambda x: x, numbers)))
    if numbers[-1] * numbers[-2] > numbers[0] * numbers[1]:
        return (numbers[-1], numbers[-2]), numbers[-1] * numbers[-2]
    else:
        return (numbers[0], numbers[1]), numbers[0] * numbers[1]

def max_product_N(numbers):
    min1 = min2 = float('-inf')
    max1 = max2 = float('inf')

    for n in numbers:
        if n < max1:
            max2 = max1
            max1 = n
        elif n < max2:
            max2 = n

        if n > min1:
            min2 = min1
            min1 = n
        elif n > min2:
            min2 = n

    if max1 * max2 > min1 * min2:
        return (max1, max2), max1 * max2
    else:
        return (min1, min2), min1 * min2

def recursive_multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + recursive_multiply(a, b - 1)

def main():
    handler()
    
if __name__ == "__main__":
    main()