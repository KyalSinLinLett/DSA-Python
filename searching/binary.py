from util import time_it

@time_it
def linear_search(number_list, number_to_find):
    for index, number in enumerate(number_list):
        if number == number_to_find:
            return index
    
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

@time_it
def binary_search_recursive(number_list, number_to_find, left_index, right_index):
    
    if left_index > right_index:
        return -1
     
    mid_index = (left_index + right_index) // 2
    
    if mid_index >= len(number_list) or mid_index < 0:
        return -1
    
    if number_list[mid_index] == number_to_find:
        return mid_index
    
    if number_list[mid_index] < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
        
    return binary_search_recursive(number_list, number_to_find, left_index, right_index)
 
if __name__ == "__main__":
    
    number_list = range(1000001)
    
    print(linear_search(number_list, 67))
    print(binary_search(number_list, 67))
    print(binary_search_recursive(number_list, 67, 0, len(number_list) -1))