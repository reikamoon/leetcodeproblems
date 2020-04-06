# Problem 1: Write a function that reverses a string.
# Restate the problem: Reverse the order of the letters in a string.
# Questions: How many characters are there?
#Assumptions: I need to reverse the order of the letters.

class Solution
    def reverse(self, s):
        def helperfunction(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right -1)

        helper(0, len(s) -1)

# My solution: Recursive function which swaps the positions from left to right to right to left and so on.
#An improved solution: Call the built in python function, reverse()
