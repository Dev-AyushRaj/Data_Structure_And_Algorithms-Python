# Modified Bubble_sort using loops
def bubble_sort(values):
    for r in range(1,len(values)-1):
        swap_flag = False
        for i in range(len(values)-r):
            if values[i] > values[i+1]:
                values[i],values[i+1] = values[i+1],values[i]
                swap_flag = True
        if not swap_flag:
            break
    return values

def selection_sort(data):
    for r in range(len(data)):
        min_index = r
        for i in range(r+1,len(data)):
            if data[i] < data[min_index]:
                min_index = i
        data[min_index],data[r]= data[r],data[min_index]
    return data

def insertion_sort(data):
    for i in range(1,len(data)):
        val = data[i]
        j = i-1
        while j >= 0 and val < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = val
    return data
        



values = [38,90,47,69,52,88,71,18,20]
bubble_sort(values)
print(values)
values = [23,67,58,97,34,21,18,57,63]
selection_sort(values)
print(values)
values = [38,90,47,69,52,88,71,18,20]
insertion_sort(values)
print(values)