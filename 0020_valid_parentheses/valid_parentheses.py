# Use a stack to keep track of brackets.
# Push opening brackets.
# If we find a matching closing bracket, we pop the opening bracket.
# At the end, we should have an empty stack.
def isValid(self, s: str) -> bool:
    stack = []
    match = {"(": ")", "[": "]", "{": "}"}
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if not stack:
                return False

            top = stack[-1]
            if c != match[top]:
                return False
            stack.pop()
        else:
            return False
    return not stack
