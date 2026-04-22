stack = []

def push(item):
    stack.append(item)
    print(item, "pushed into stack")

def safe_pop():
    if len(stack) == 0:
        print("Stack is empty, nothing to pop.")
        return None
    return stack.pop()


# Example usage
push(10)
push(20)
push(30)

print("Popped:", safe_pop())
print("Popped:", safe_pop())
print("Popped:", safe_pop())
print("Popped:", safe_pop())  # empty case