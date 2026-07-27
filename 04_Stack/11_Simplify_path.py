"""
LeetCode 71. Simplify Path

Key Idea:-
    Use a stack to simulate directory navigation in a Unix-style file system.
    Ignore empty directory names and "." since they represent the current directory.
    When ".." is encountered, move up one directory by removing the last valid directory from the stack.
    Otherwise, push valid directory names onto the stack.
    Finally, join the remaining directories to form the simplified canonical path.

Approach:-
    1.Initialize an empty stack to store valid directory names.
    2.Traverse the path character by character, building each directory name.
    3.Whenever a '/' is encountered:
        If the current directory is "..":
            Pop the last directory from the stack if it exists.
        If the current directory is "." or empty:
            Ignore it.
        Otherwise:
            Push the directory name onto the stack.
    4.Reset the current directory after processing each '/'.
    5.Join all directory names in the stack with '/' and prepend a leading '/'.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Stack to store valid directory names
        stack = []

        # Stores the current directory name while parsing
        curr = ""

        # Add an extra '/' to process the last directory
        for c in path + "/":

            if c == "/":

                # Move to the parent directory
                if curr == "..":
                    if stack:
                        stack.pop()

                # Ignore empty strings and current directory "."
                elif curr != "" and curr != ".":
                    stack.append(curr)

                # Reset for the next directory
                curr = ""

            else:
                # Build the current directory name
                curr += c

        # Construct the simplified canonical path
        return "/" + "/".join(stack)

"""
Time Complexity:-
                O(n)
Space Complexity:-
                O(n)
"""