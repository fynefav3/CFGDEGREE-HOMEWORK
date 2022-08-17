

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