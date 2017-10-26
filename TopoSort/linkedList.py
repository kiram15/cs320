class Node(object):

    def __init__(self, data=None, color='W', nextNode=None):
        self.data = data
        self.color = color
        self.next_node = nextNode

    def getData(self):
        return self.data

    def getColor(self):
        return self.color

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.next_node = newNext

class LinkedList(object):
    def __init__(self, color, head=None):
        self.head = head

    def insert(self, data, color):
        newNode = Node(data, color)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
