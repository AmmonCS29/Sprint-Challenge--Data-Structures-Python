class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        current = node #assigns the parameter node to be the current node. 
        if current is None: #Checking to see if node called in the parameters is none
            return None #if it is none return none
        if current.get_next() ==  None: #Checking to see if the next node in the list is none
            self.head = current #If the next node is none. Set self.head to be the current node
            self.head.next_node = prev #Setting the next_node pointer at the previous node. 
            return #This returns the function and ends it. 
        self.reverse_list(current.get_next(), node ) #inputing the next node as the argument for node and the current node as the argument for prev.
        current.next_node = prev #This flips the pointer from the current next node to the previous node. 
        
        # node = self.head
        # prev = self.head.next_node
        # if node is None:
        #     return 
        # if node.next_node:
        #     node.get_next()
        #     print("if", node.value)
        # else:
        #     self.head = node
        #     print("else",node)            


