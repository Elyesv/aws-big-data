import time

def handler():

    with open('text_light.txt', 'r') as file:
        text = file.read().replace('\n', '').replace('.', '').replace(',','').lower()
        list_words = text.split(' ')
    
        len_list_words = len(list_words)
        print('Number of words in the text: ', len_list_words)
        
        print('-' * 50)
        
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

        start_time = time.time()
        for _ in range(50):
            sorted_list = shell_sort(list_words)
            # print(sorted_list)
        end_time = time.time()
        print('Average execution time to sort the list (shell sort): ', (end_time - start_time), 'seconds')
        
        print('-' * 50)
        
        start_time = time.time()
        for _ in range(50):
            sorted_list = quick_sort(list_words)
            # print(sorted_list)
        end_time = time.time()
        print('Average execution time to sort the list (quick sort): ', (end_time - start_time), 'seconds')
        
        print('-' * 50)
        
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

def main():
    handler()
    
if __name__ == "__main__":
    main()