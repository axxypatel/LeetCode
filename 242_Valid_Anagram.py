"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashTable = {}
        for i in s:
            if i not in hashTable:
                hashTable[i] = 1
            else:
                hashTable[i] += 1
                
        for j in t:
            if j not in hashTable:
                return False
            
            hashTable[j] -= 1
            if hashTable[j] <= 0:
                del hashTable[j]
        return True
        
            
        
