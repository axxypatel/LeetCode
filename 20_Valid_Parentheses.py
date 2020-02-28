"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l < 1: return True
        if l == 1: return False
        stack = []
        pointer = 0
        for i in range(l):
            if s[i] == '(':
                stack.append('(')
                pointer+=1
            elif s[i] == '[':
                stack.append('[')
                pointer+=1
            elif s[i] == '{':
                stack.append('{')
                pointer+=1
            elif s[i] == ')' and pointer != 0 :
                if stack[pointer-1] == '(':
                    stack.pop()
                    pointer-=1
                else:
                    stack.append(')')
            elif s[i] == ']' and pointer != 0 :
                if stack[pointer-1] == '[':
                    stack.pop()
                    pointer-=1
                else:
                    stack.append(']')
            elif s[i] == '}' and pointer != 0 :
                if stack[pointer-1] == '{':
                    stack.pop()
                    pointer-=1
                else:
                    stack.append('}')
            else:
                return False
        if len(stack) < 1:
            return True
        else:
            return False
            
        
