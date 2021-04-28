array = [4, 5, 7, 3, 2, 9, 1, 8, 6, 10]

def bubbleSort(array): 
    switch = True
    while switch:
        switch = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                switch = True
    return array

print(bubbleSort(array))
print(sorted(array))