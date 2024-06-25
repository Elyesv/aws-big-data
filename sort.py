import time

def handler():

    with open('texte.txt', 'r') as file:
        text = file.read().replace('\n', '').replace('.', '').replace(',','').lower()
        list_words = text.split(' ')
    
        # len_list_words = len(list_words)
        # print('Number of words in the text: ', len_list_words)
        
        sorted_list = bubble_sort([1,2,9,3,8,4,5,7,6])
        print(sorted_list)

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