import time

def handler():

    with open('text_light.txt', 'r') as file:
        text = file.read().replace('\n', '').replace('.', '').replace(',','').lower()
        list_words = text.split(' ')
    
        # len_list_words = len(list_words)
        # print('Number of words in the text: ', len_list_words)
        
        start_time = time.time()
        for _ in range(1):
            sorted_list = bubble_sort(list_words)
            # print(sorted_list)
        end_time = time.time()
        print('Average execution time to sort the list: ', (end_time - start_time), 'seconds')


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr            
        


def main():
    handler()
    
if __name__ == "__main__":
    main()