# problem:
# given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'
# The input string s is valid if and only if:
#   Every open bracket is closed by the same type of close bracket
#   Open brackets are closed in the correct order
#   Every close bracket has a corresponding open bracket of the same type
# Return true if s is a valid string, and false otherwise.
# 
# O(n) soln:
# use a stack!
# if is opening bracket => add to stack
# if is closing bracket => check top of stack to match -> if match remove
# if all removed -> will be empty string so is true
# for parenthesis in s:
#   if p is in closetoopen: then it is closing bracket
#       check if stack exists and top of stack matches closing bracket:
#       # if stack doesn't exist then it starts with closing bracket so cannot be valid
#       # or if don't match then cannot be valid
#           pop bracket at top of stack
#       else:
#           return False
#   else:
#       add opening bracket to stack
# if stack == []:
#   return True
# else:
#   return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {")":"(", "]":"[", "}":"{"}

        for p in s:
            if p in closetoopen:
                if stack and stack[-1] == closetoopen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return True if stack == [] else False