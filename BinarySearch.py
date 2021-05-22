def search_num(start, end, array, target):
    arr_len = (end + start)+1       # mistake here, did --> end-start
    mid = arr_len // 2
    number = array[mid]
    
    print(number, target, mid, start, end)
    if number == target:
        return mid
    elif start >= end:
        return -99
    
    if number > target:
        return search_num(start, mid - 1, array, target)
    elif number < target:
        return search_num(mid + 1, end, array, target)
