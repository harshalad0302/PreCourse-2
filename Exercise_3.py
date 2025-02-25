# Node class
# T.C = O(N)
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node in the LinkedList


class LinkedList:

    def __init__(self):
        self.head = None  # initialize linked list with head pointer

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node  # Update the head to the new node

    # Function to get the middle of
    # the linked list

    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while slow_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # slow_ptr will be pointing to the middle node
        if slow_ptr is not None:
            print(f"The middle element is: {slow_ptr.data}")
        else:
            print("The linked list is empty.")


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
