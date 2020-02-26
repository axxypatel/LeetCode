"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
      Input: 5
      Output:
      [
           [1],
          [1,1],
         [1,2,1],
        [1,3,3,1],
       [1,4,6,4,1]
      ]
      
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        temp = []
        for i in range(numRows):
            temp2 = []
            j = 0
            while j <= i:
                if j == 0 or j == i :
                    temp2.append(1)
                else:
                    temp2.append(temp[i-1][j-1]+ temp[i-1][j])
                j += 1 
            temp.append(temp2)
        return temp                
        
