#Problem 2: Given an array of characters, compress it in place.
#Restate the Problem: Find a way to make the array a shorter length.
#Questions: how many elements are in the array?
#Assumptions: I need to make sure that all the elements stay but make the array a shorter length.

def compress(chars):
    '''Time Complexity is O(N) where n is the length of the characters'''
    anchor = write = 0 #Anchor is starting position
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
                anchor = read + 1
            return write

#My solution: Start from a position, and read left from right. Once at the end (write),
#chars[anchor] will be the correct character and the length if greater than 1, will be read - anchor + 1.
