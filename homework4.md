# Big(0)Notation
# Time complexity = O(n^2)
This algorithm is said to have a non-linear time complexity where the
running time increases non-linearly (n^2)with the length of the input. 
The function above is a nested loop and nested loops come under this order.
This is a Quadratic Time.
# Space Complexity 0(n) = Linear Time
The memory space of the algorithm does not grow with the iteration. 
 arrLen = len(numbers); allocates the memory space of 4 bytes.
 for i in range(0, arrLen): allocates a memory space of 4 bytes.
  for j in range(i+1, arrLen): allocates a memory space of 4 bytes.
  The return statement allocates a memory space of 4 bytes also.
  The final spce complexity will be fS(n) = n + 16 = 0(n). 