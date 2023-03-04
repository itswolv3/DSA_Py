from stack_constructor import Stack
from empty_stack_constructor import EmptyStack


def reverse_string(string: str) -> str:
    string_stack = EmptyStack()
    for i in string:
        string_stack.push(i)

    res = []
    for _ in range(string_stack.size()):
        res.append(string_stack.pop())

    return "".join(res)


def reverse_string2(string):
    stack = EmptyStack()
    reversed_string = ""
    for char in string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


def is_balanced_parenthesis(string: str) -> bool:
    parens_stack = EmptyStack()
    for i in string:
        parens_stack.push(i)

    return parens_stack.size() % 2 == 0


def is_balanced_parentheses2(parentheses):
  stack = Stack()
  for p in parentheses:
    if p == '(':
      stack.push(p)
    elif p == ')':
      if stack.is_empty() or stack.pop() != '(':
        return False
  return stack.is_empty()
    

def sort_stack(stack):
    additional_stack = EmptyStack()
    while not stack.is_empty():
        temp = stack.pop()
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())
        additional_stack.push(temp)
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())
            
        
print(reverse_string("hello"))
print(is_balanced_parenthesis("(())"))
print(is_balanced_parenthesis("((())"))
print(is_balanced_parenthesis("(hello(This(is)a)test"))
print(is_balanced_parenthesis("(hello(This(is)a)test)"))
stack = EmptyStack()
stack.push(2)
stack.push(5)
stack.push(1)
stack.push(3)
stack.push(10)
stack.push(4)

sort_stack(stack)
stack.print_list()
