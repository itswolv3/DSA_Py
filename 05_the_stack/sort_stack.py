    def sort_stack(stack):
        # Create a new stack to hold the sorted elements
        additional_stack = Stack()
     
        # While the original stack is not empty
        while not stack.is_empty():
            # Remove the top element from the original stack
            temp = stack.pop()
     
            # While the additional stack is not empty and 
            #the top element is greater than the current element
            while not additional_stack.is_empty() and additional_stack.peek() > temp:
                # Move the top element from the additional stack to the original stack
                stack.push(additional_stack.pop())
     
            # Add the current element to the additional stack
            additional_stack.push(temp)
     
        # Copy the sorted elements from the additional stack to the original stack
        while not additional_stack.is_empty():
            stack.push(additional_stack.pop())


# Time complexity: 0(n^2)
