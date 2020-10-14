def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) == 0: return False
                if stack[-1] == '(' and c != ')': return False
                if stack[-1] == '{' and c != '}': return False
                if stack[-1] == '[' and c != ']': return False
                stack.pop()
        if len(stack) > 0: return False
        return True
