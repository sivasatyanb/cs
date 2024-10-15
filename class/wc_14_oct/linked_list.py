class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtIndex(self, data, index=None):
        new_node = Node(data)
        
        if index == 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        # if no index is given, it is assumed that the data will be added to the end of the linked list
        if index is None:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            return
        
        current_node = self.head
        position = 0
        while current_node and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print('Index not present')

    def removeAtIndex(self, index=None):
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        # if no index is given, it is assumed that the data will be removed from the end of the linked list
        if index is None:
            if self.head.next is None:
                self.head = None
                return
            current_node = self.head
            while current_node.next and current_node.next.next:
                current_node = current_node.next
            current_node.next = None
            return
        
        current_node = self.head
        position = 0
        while current_node and current_node.next and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node and current_node.next:
            current_node.next = current_node.next.next
        else:
            print('Index is not available')

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node and position != index:
            position += 1
            current_node = current_node.next

        if current_node:
            current_node.data = val
        else:
            print('Index is not available')

    def printLL(self):
        size = 0
        data = []
        current_node = self.head
        while current_node:
            size += 1
            data.append(current_node.data)
            current_node = current_node.next
        print('Linked list:')
        print(*data)


llist = LinkedList()

llist.insertAtIndex('a')
llist.insertAtIndex('b')
llist.insertAtIndex('c', 0)
llist.insertAtIndex('d')
llist.insertAtIndex('f', 2)
llist.updateNode('z', 4)
llist.removeAtIndex()
llist.printLL()