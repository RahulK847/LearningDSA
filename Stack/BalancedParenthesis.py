# Check for Balanced Parenthesis
# six possible characters in I/P string: (, ), {, }, [ and ]
# I/P -> "([])"  |    "((()))"  |   "([)]"   |     "{}([()])"   |    "(()))"     |
# O/P ->  Yes    |      Yes     |    NO      |       Yes        |      NO        |

def isValid(s):
    stack = []
    closeToOpen = {"}": "{", "]": "[", ")": "("}
    for i in s:
        if i in closeToOpen:
            if stack and stack[-1] == closeToOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False


