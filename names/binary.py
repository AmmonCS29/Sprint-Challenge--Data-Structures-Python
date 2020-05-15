"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # insert adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    def insert(self, value):
        if self.value is None:
            root = BSTNode(value) # created root not
            self.value = root.value # assigned value to root value
        
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
                # print("self.left", self.left.value)
            else:
                self.left.insert(value)
        
        else:
            if not self.right:
                self.right = BSTNode(value)
                # print("self.right", self.right.value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
         # when we start searching, self will be the root
        # compare the target against self
        # 
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_num = self.value
        # if self.right == None:
        #     return max_num
        # else:
        #     while self.right is not None: 
        #         if self.right.value > max_num:
        #             max_num = self.right.value
        #         return max_num    
        if self.right:
            return self.right.get_max()
        else:
            return max_num

    # # Call the function `fn` on the value of each node
    # for_each performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work.
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.right.in_order_print(node.right)

        # if self.left:
        #     self.left.in_order_print(self.left)
        
        # print(node.value)
        
        # if self.right:
        #     self.right.in_order_print(self.right)
        # res = ''
        # if node:
        #     res = self.in_order_print(node.left)    
        #     res += str(node.value) + "\n"
        #     res = res + self.in_order_print(node.right)
        # return res

        # if node:
        #     node.in_order_print(node.left)
        #     print(node.value)
        #     node.in_order_print(node.right)

        # res = []
        # if node:
        #     res = node.in_order_print(node.left)
        #     res.append(node.value)
        #     res = res + node.in_order_print(node.right)
        # return res
        

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # from queue import SimpleQueue
    def bft_print(self, node):

        queue = deque()
        # add the root node
        queue.append(self)

        # loop so long as the stack still has elements 
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

        # to_print = SimpleQueue()
        # to_print.put(node)
        # while to_print.qsize() != 0:
        #     self = to_print.get()
        #     if self.left is not None:
        #         to_print.put(self.left)
        #     if self.right is not None:
        #         to_print.put(self.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    def dft_print(self, node):

        stack = [] 
        # add the root node
        stack.append(node)

        # loop so long as the stack still has elements 
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            # if current.left:
            #     stack.append(current.left)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            
    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)
    # # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)    
        # if node:
        #     node.post_order_dft(node.left)
        #     node.post_order_dft(node.right)
        #     print(node.value)
            
