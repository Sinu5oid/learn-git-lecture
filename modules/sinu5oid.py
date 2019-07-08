from random import randint

def bubbleSort(list):
    # to not mutate input list
    result = list.copy()
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
    return result

def generateListWithCustomLength(len):
    return [randint(0, 10) for i in range(len)]

# if runs as standalone module
if __name__ == "__main__":
    list = generateListWithCustomLength(10)

    print('Unsorted list')
    print(list)

    sorted_list = bubbleSort(list)
    print('Sorted list')
    print(sorted_list)
    print('Origin list didn\'t change')
    print(list)