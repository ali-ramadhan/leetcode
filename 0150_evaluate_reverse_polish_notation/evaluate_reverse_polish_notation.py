# O(n^2) worst case solution using a double loop.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        while len(tokens) > 1:
            for i, t in enumerate(tokens):
                if t in ops:
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    
                    if t == "+":
                        tokens[i] = str(a + b)
                    elif t == "-":
                        tokens[i] = str(a - b)
                    elif t == "*":
                        tokens[i] = str(a * b)
                    elif t == "/":
                        tokens[i] = str(int(a / b))
                    
                    del tokens[i-1]
                    del tokens[i-2]
                    break
                else:
                    continue

        return int(tokens[0])

# O(n) solution using a stack.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "*":
                    stack.append(l * r)
                elif t == "/":
                    stack.append(int(l / r))
        
        return stack.pop()
                    
