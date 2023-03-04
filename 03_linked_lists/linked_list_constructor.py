class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value) 
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        ''' 
        Prints Linked List.
        '''
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        '''
        Parameters:
        value: Desired value to be added
        Takes value, adds to end of list
        '''
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        '''
        Remove last item from list
        '''
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next != None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
                
    def preppend(self, value):
        ''' 
        Parameters:
        value: The desired value to be added.
        Adds value to the beginning of the list.
        '''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        '''
        Remove first item from list.
        '''
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
      
    def get(self, index):
        '''
        Parameters:
        index: int: Index of desired node.
        Returns item at given index position.
        '''
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, value, index):
        '''
        Parameters:
        value: Desired new value for the index.
        index: int: Index position of value to be changed.
        Change the value of an item at given index position.
        '''
        temp = self.get(index)
        if temp != None:
            temp.value = value
            return True
        return False

    def insert(self, value, index):
        '''
        Parameters:
        value: value to be inserted into the linked list
        index: int: index to be queried
        Insert a new value at desired index position.
        '''
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.preppend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        '''
        Parameters: index: int
        Removes node from given index position.
        '''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp  = pre.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        '''
        Reverses the linked list
        '''
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        '''
        Returns the middle node
        '''
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def remove_ducplicates(self):
        '''
        Checks for duplicates, will remove if found
        '''
        values = set()
        previous = None
        current = self.head
        while current != None:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = currentc
            current = current.next


def find_kth_from_end(ll, k):
    '''
    Parameters:
    ll: A linked list
    k: int: kth point from the end

    Returns the node queried
    '''

    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow

