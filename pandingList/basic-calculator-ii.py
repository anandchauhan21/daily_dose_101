"""
basic-calculator-ii
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

Question link https://leetcode.com/problems/basic-calculator-ii/
"""
import math


class Solution:

    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        pre_op = '+'
        s += '+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                pass
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append((operant * num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant / num))
                num = 0
                pre_op = c
        return sum(stack)
