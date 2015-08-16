class Node:
    def __init__(self, val):
        self.val = val
        self.nextNode = None
    

class LinkedList:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            runner = self.root
            while runner.nextNode:
                runner = runner.nextNode
            runner.nextNode = Node(val)
    
    def delete(self, val):
        if self.root:
            if self.root.val == val:
                self.root = self.root.nextNode
            else:
                runner = self.root
                while runner.nextNode:
                    if runner.nextNode.val == val:
                        del_node = runner.nextNode
                        runner.nextNode = runner.nextNode.nextNode
                        del(del_node)
                    else:
                        runner = runner.nextNode
    
    def printLinkedList(self):
        if not self.root:
            print('The linked list is empty!')
        runner = self.root
        while runner:
            print(runner.val)
            runner = runner.nextNode
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    print('********Should print 1 through 5')
    ll.printLinkedList()
    print('********************************')
    
    ll.delete(3)
    print('********Should print 1,2,4,5****')
    ll.printLinkedList()
    print('********************************')
    
    ll.delete(1)
    print('********Should print 2,4,5******')
    ll.printLinkedList()
    print('********************************')
    
    ll.delete(5)
    print('********Should print 2,4********')
    ll.printLinkedList()
    print('********************************')
    
    ll.delete(15)
    print('********Should print 2,4********')
    ll.printLinkedList()
    print('********************************')
    
    ll.insert(15)
    print('********Should print 2,4,15*****')
    ll.printLinkedList()
    print('********************************')
    
    ll.delete(2)
    ll.delete(4)
    ll.delete(15)
    
    print('********Should not print********')
    ll.printLinkedList()
    print('********************************')
