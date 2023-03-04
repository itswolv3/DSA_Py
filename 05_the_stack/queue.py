class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.value = new_node
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        '''
        Prints out the queue.
        '''
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        '''
        Paratmeters: 
        value: Desired value to add.

        Adds the desired value to end of the queue.
        '''
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        '''
        Removes the last item in the queue.
        '''
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
