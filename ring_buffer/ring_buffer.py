# from queue1 import Queue
# from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity  = capacity
        self.storage = []

    class __Full:
        def __init__(self, n):
            raise

        def append(self, x):
            self.storage[self.cur] = x
            self.cur = (self.cur+1) % self.capacity

        def get(self):
            return self.storage

    def append(self, item): # check to see if the list is at full capacity/ adds new value (item)
        self.storage.append(item)
        if len(self.storage) == self.capacity:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
            return self.storage
  
    




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def append(self, data):
#         new_node = Node(data)
#         self.length += 1
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             new_node.next = self.head
#         elif self.length == self.capacity:
#             if self.head is None:
#                 return None
#             else: 
#                 # value = self.head.value
#                 self.head = self.head.next
#                 self.tail.next = new_node
#                 self.tail = new_node
#                 self.tail.next = self.head
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#             self.tail.next = self.head
    
#     def get(self):
#         current = self.head
#         if self.head is None:
#             print("Ring buffer is empty")
#             return
#         else:
#             print("Ring Buffer list")
#             print(current.data)
#             while current.next != self.head:
#                 current = current.next
#                 print(current.data)




# class RingBuffer:


#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.queue = [None] * capacity 
#         self.tail = -1
#         self.head = 0
#         self.size = 0

#     def append(self, item):

#         if self.size == self.capacity:
#             print("Error: Queue is Full")
        
#         else:
#             self.tail = (self.tail + 1) % self.capacity
#             self.queue[self.tail] = item
#             self.size += 1
        
#     def Dequeue(self):
#         if self.size == 0:
#             print("Error : Queue is empty")
#             return 
        
#         else:
#             tmp = self.queue[self.head]
#             self.head = (self.head + 1) % self.capacity

#         self.size = self.size -1
#         return tmp
    
#     def get(self):

#         if self.size == 0:
#             print("queue is Empty \n")

#         else:
#             index = self.head

#             for i in range(self.size):
#                 print(self.queue[index])
#                 index = (index + 1) % self.capacity


    # def append(self, item):
    #     if self.length == self.capacity:
    #         self.storage.popleft()
    #         self.storage.append(item)
    #         # print("if", item)
    #     else:
    #         self.storage.append(item)
    #         self.length += 1
    #         # print("else", item)      
    
    # def get(self):
    #     for i in self.storage:
    #         if not None:
    #             self.value.append(i)
    #     return print(self.value)
         
    # def __init__(self, capacity):
    #     self.capacity = capacity
    #     self.storage = Queue()
    #     self.length = 0
    #     self.value = []
        

    # def append(self, item):
    #     if self.length == self.capacity:
    #         self.storage.dequeue()
    #         self.storage.enqueue(item)
    #         # print("if", item)
    #     else:
    #         self.storage.enqueue(item)
    #         self.length += 1
    #         # print("else", item)      
               

    # def get(self):
    #     for i in self.storage:
    #         if not None:
    #             self.value.append(i)
    #     return print(self.value)

    # def get(self):
    #     current = self.storage.head
    #     while current.next is not None:
    #         self.value.append(current.value)
    #         current = current.next
    #         print(self.value)
           

        

rb = RingBuffer(5)
for i in range (50):
    rb.append(i)

rb.get()
# rb.append('a')
# rb.append('b')
# rb.append('c')
# rb.append('d')
# rb.append('e')
# rb.append('f')
# rb.append('g')
# rb.append('h')
# print(rb.get())

