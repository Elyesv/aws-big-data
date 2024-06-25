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

def main():
    handler()
    
if __name__ == "__main__":
    main()