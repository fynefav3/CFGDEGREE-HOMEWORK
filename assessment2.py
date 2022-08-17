
# algorithm 1

# # O(n) time complexity is linear time since the running time increases linearly with the length of the input
# O(1) space No extra space is needed as the indices can be stored in constant space.
def isValidSubsequence(array, sequence):
	sequenceIndex = 0
	for value in array:
		if sequenceIndex == len(sequence):
			break
		if sequence[sequenceIndex] == value:
			sequenceIndex += 1
	return sequenceIndex == len(sequence)

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(isValidSubsequence([5, 8, 3, -2, 4], [8]))
print(isValidSubsequence([1, 2, 8, -1, 0, 3, 9], [2, -1, 0, 11, 3]))



# algorithm 2
#Time complexity O(n^2) space complexity 0(1) this is a bubble sort algorithm
# having to iterate all numbers t be sure of which number 
# is the largest is really time consuming and a worst case scenario.
def findThreeLargestNumbers(array):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]
    n = len(array)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if array[i - 1] > array[i]:
                swap(i - 1, i)
                swapped = True
    return array


array1 = [141, 1, 17, -7, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array1))
print(array1[-3:])

array2 = [3, 1, 2]
print(findThreeLargestNumbers(array2))
print(array2[-3:])

array3 = [142, 6, 34, 67, 31, -2, -5, 8]
print(findThreeLargestNumbers(array3))
print(array3[-3:])

array4 = [-4, 0, -2, -8, -142, -2, -8]
print(findThreeLargestNumbers(array4))
print(array4[-3:])

