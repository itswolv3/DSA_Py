class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        '''
        Prints out the entire list.
        '''
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        '''
        Parameters:
        value: A value to add to the list.

        Adds the value to the end of the list
        '''
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.lenght += 1
        return True

    def pop(self):
        '''
        Removes the last item from the list
        '''
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
             self.tail = self.tail.prev
             self.tail.next = None
             temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        '''
        Parameters: 
        value: Desired value to be added.

        Adds value to the begining of the list
        '''
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        '''
        Removes the first item in the list
        '''
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        '''
        Parameters:
        index: int: Desired index to be queried.

        Returns the item at index position provided.
        '''
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:     
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, value, index):
        '''
        Parameters:
        value: Desired value to be set.
        index: Index position to set value.

        Sets the value provided at the index position provided.
        '''
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, value, index):
        '''
        Parameters:
        value: Desired value to be added.
        index: int: Index position to add new value at.

        Adds the new value at the given index position.
        '''
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True


    def remove(self, index):
        '''
        Parameters:
        index: int: Index provided of item to be removed.

        Returns removed item at the provided index position. 
        '''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return pop_first()
        if index == self.length - 1:
            return pop()

        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next  = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    def swap_first_last(self):
        '''
        Swaps the values of the first and last item of the list.
        '''
        if self.head is None or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value

    def reverse(self):
        '''
        Reverse the doubly linked list.
        '''
        temp = self.head
        while temp is not None:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev

        self.head, self.tail = self.tail, self.head

    def is_palindrome(self):
        '''
        Returns True or False depending on if the list is a palindrome.
        '''
        if self.lenght <= 1:
            return True
        forward_node = self.head
        backward_node = self.tail
        for _ in range(self.lenght // 2):
            if forward_node.value != backward_node.value:
                return False
            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True
