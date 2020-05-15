"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node
    self.next = None

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class Queue:
    def __init__(self):
        # self.size = 0
        # self.storage = list()
        self.head = None
        self.last = None
    
    def __len__(self):
    ## Step 1: Array Method     
        # return len(self.storage)
    ## Step 2: Linked List
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length
    
        
    def enqueue(self, value):
    ## Step 2: Linked List
        if self.last is None: 
            self.head = Node(value)
            self.last = self.head
        else: 
           self.last.next = Node(value)
           self.last = self.last.next
        ## Step 1: Array Method     
        # return self.storage.append(value)
        


    def dequeue(self):
    ## Step 2: Linked List
        if self.head is None: 
            return None
        else: 
            value = self.head.value
            self.head = self.head.next
            return value
        ## Step 1: Array Method     
        # if self.storage:
        #     return self.storage.pop(0)            
        # else: 
        #     return None
        

