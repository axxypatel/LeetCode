"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""
### Horizontal Method
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: return ""
        elif len(strs) == 1: return strs[0]
        prefix = ""
        prev = strs[0]
        #print(prev[0])
        for i in range(1,len(strs)):
            j = 0
            prefix = ""
            curr = strs[i]
            print(curr)
            while j < len(prev) and j < len(curr) and prev[j] == curr[j]:
                prefix += prev[j]
                j += 1
            prev = prefix
        return prefix
"""
### Vertical method
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: return ""
        elif len(strs) == 1: return strs[0]
        prefix = strs[0]
        for i in range(len(prefix)):
            temp = prefix[i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or temp != strs[j][i]:
                    return prefix[:i]
        return prefix         
"""
### Divide and Conquer Method

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def commonPrefix(leftStr,rightStr):
            m = min(len(leftStr),len(rightStr))
            for i in range(m):
                if leftStr[i] != rightStr[i]:
                    return leftStr[:i]
            return leftStr[:m]
            
        def divideAndConq(strs,left,right):
            if(left == right):
                return strs[left]
            else:
                mid = math.floor((left + right) / 2)
                lcpLeft = divideAndConq(strs,left,mid)
                lcpRight = divideAndConq(strs,mid+1,right)
                return commonPrefix(lcpLeft,lcpRight)
            
        if len(strs) < 1: return ""
        elif len(strs) == 1: return strs[0]
        
        left,right = 0,len(strs) -1 
        
        return divideAndConq(strs,left,right)

            
                
                
            
        
        
                
                
            
        
        
