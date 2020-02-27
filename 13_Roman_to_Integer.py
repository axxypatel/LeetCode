"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

""" Old Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        final_numb = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i + 1 < l:
                    if s[i+1] == "V":
                        final_numb += 5-1
                        i+=1
                    elif s[i+1] == "X":
                        final_numb += 10-1
                        i+=1             
                    else:
                        final_numb += 1
                else:
                    final_numb += 1
            elif s[i] == "X":
                if i + 1 < l:
                    if s[i+1] == "L":
                        final_numb += 50-10
                        i+=1
                    elif s[i+1] == "C":
                        final_numb += 100-10
                        i+=1
                    else:
                        final_numb += 10                  
                else:
                    final_numb += 10
            elif s[i] == "C":
                if i + 1 < l:
                    if s[i+1] == "D":
                        final_numb += 500-100
                        i+=1
                    elif s[i+1] == "M":
                        final_numb += 1000-100
                        i+=1
                    else:
                        final_numb += 100                    
                else:
                    final_numb += 100
            elif s[i] == "V":
                final_numb += 5
            elif s[i] == "L":
                final_numb += 50
            elif s[i] == "D":
                final_numb += 500
            elif s[i] == "M":
                final_numb += 1000
            else:
                final_numb += 0
            i+=1
        return final_numb

"""            

class Solution:
    def romanToInt(self, s: str) -> int:
        final_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        final_val = 0
        l = len(s)
        i =0
        while i < l:
            if i+1 < l:
                if final_dict[s[i]] < final_dict[s[i+1]]:
                    final_val += final_dict[s[i+1]] - final_dict[s[i]]
                    i+=1
                else:
                    final_val += final_dict[s[i]]
            else:
                final_val += final_dict[s[i]]
            i+=1
            
        return final_val
