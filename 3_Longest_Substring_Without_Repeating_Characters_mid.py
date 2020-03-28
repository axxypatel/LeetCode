"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""
## Sliding window solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        n = len(s)
        ans,i,j = 0,0,0
        while (i < n and j < n):
            if s[j] not in hashSet:
                hashSet.add(s[j])
                j += 1
                ans = max(ans,j-i)
                
            else:
                hashSet.remove(s[i])
                i += 1
        return ans
# With improvements in window function

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        n = len(s)
        i,j,ans = 0,0,0
        while j < n:
            if s[j] in hashMap:
                i = max(hashMap[s[j]],i)
            ans = max(ans,j-i+1)
            hashMap[s[j]] = j + 1
            j += 1
        return ans
        
        
