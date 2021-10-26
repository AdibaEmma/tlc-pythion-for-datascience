# def shiftArray(arr):
#     last_element = arr.pop()
#     arr.insert(0, last_element)
#     return arr
#
# print(shiftArray([5,7,8,2]))


def arrayWithIndicies(arr, indices):
    return [arr[i] for i in indices]
print(arrayWithIndicies([1,5,6,8,3,4], [3,2,1]))
