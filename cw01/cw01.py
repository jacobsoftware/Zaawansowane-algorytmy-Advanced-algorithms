class Node:
    def __init__(self, value=None):       
        self.value = value
        self.nextNode = None
        self.prevNode = None
              

class List:

    def __init__(self):
        self.head = None
        self.tail = None
        print('/*inicjuje zmienne*/')
    
    def list_insert(self,key):
        #node = type('Node',(),{'value':key,'nextNode':None,'prevNode':None})
        new_node = Node(key)

        if self.head is None:          
            self.head = new_node
            self.tail = new_node

        else:
            new_node.nextNode = self.head
            self.head.prevNode = new_node
            self.head = new_node

    def write(self):
        node = self.head
        string = '//'

        while node:           
            string = string +  str(node.value) + ' '
            node = node.nextNode 

        print(string)

    def list_search(self,key):
        node = self.head
        if_empty = True

        while node:
            if node.value == key:
                if_empty = False
                print(node.value)

            node = node.nextNode

        if if_empty:
            print('// -1')

    def list_insert_after(self,key,after):
        node = self.head

        while node:
            if node.value == after:
                new_node = Node(key)
                new_node.nextNode = node.nextNode

                if node.nextNode:
                    node.nextNode.prevNode = new_node

                else:
                    self.tail = new_node

                node.nextNode = new_node
                new_node.prevNode = node

            node = node.nextNode

    def list_delete(self,key):
        node = self.head

        while node:
            if node.value == key:

                if node.prevNode:
                    node.prevNode.nextNode = node.nextNode

                # lista 1 lub 0 elementowa
                else:
                    self.head = node.nextNode 

                if node.nextNode:
                    node.nextNode.prevNode = node.prevNode

                # lista 0 elementowa
                else:
                    self.tail = node.prevNode

            node = node.nextNode

    def list_insert_before(self,key,before):
        node = self.head

        while node:
            if node.value == before:
                new_node = Node(key)
                new_node.prevNode = node.prevNode

                if node.prevNode:
                    node.prevNode.nextNode = new_node
                    
                else:
                    self.head = new_node

                node.prevNode = new_node
                new_node.nextNode = node

            node = node.nextNode

    
    def clear(self):
        self.head = None
        self.tail = None
        return print('/*zwalnia pamięć*/')
    

def zadanie1():
    L = List()
    L.write()
    L.list_insert(1)
    L.list_insert(2)
    L.write()
    L.list_insert(3)
    L.list_search(2)
    L.list_search(4)
    L.list_insert_after(4,2)
    L.write()
    L.list_delete(2)
    L.write()
    L.list_delete(5)
    L.write()
    L.list_insert_before(5,3)
    L.write()
    L.clear()
    L.write()


class Stack():
    def __init__(self):
        self.data = List()
        self.top = 0 

    def stack_empty(self):
        if self.top is 0: return True
        else: return False
    
    def push(self,key):
        self.data.list_insert(key)
        self.top = self.top + 1

    def pop(self):
        if self.top is not 0:
            top_value = self.data.head.value
            string = '//'+str(top_value)
            self.data.list_delete(top_value)
            self.top = self.top - 1
            return string
        else:
            return '//niedomiar'

def zadanie2():  
    S = Stack()
    S.push(1)
    S.push(2)
    S.data.write()
    S.push(3)
    S.data.write()
    print(f'//{S.stack_empty()}')
    print(S.pop())
    print(S.pop())
    S.data.write()
    print(S.pop())
    print(S.pop())
    S.data.write()
    print(f'//{S.stack_empty()}')

class Queue():
    def __init__(self):
        self.data = List()
        self.length = 10
        self.head = 1
        self.tail = 1

    def queue_empty(self):
        if self.head == self.tail: return True
        else: return False

    def enqueue(self,key):
        if self.tail  == self.length: 
            return '//przesycenie' 
        elif self.head == 1 and self.tail == 1:
            self.data.list_insert(key)
            self.tail = self.tail + 1
        else:
            self.data.list_insert_after(key,self.data.tail.value)
            self.tail = self.tail + 1

    def dequeue(self):
        if self.queue_empty():
            return 'niedomiar'
        else:
            removed_value = self.data.head.value
            self.data.list_delete(self.data.head.value)
            self.head = self.head + 1
            return removed_value

def zadanie3():
    Q = Queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.data.write()
    Q.enqueue(3)
    Q.data.write()
    print(f'//{Q.queue_empty()}')
    print(f'//{Q.dequeue()}')
    print(f'//{Q.dequeue()}')
    Q.data.write()
    print(f'//{Q.dequeue()}')
    print(f'//{Q.dequeue()}')
    Q.data.write()
    print(f'//{Q.queue_empty()}')

if __name__ == '__main__':
    print('Zadanie 1: \n')
    zadanie1()
    print('\nZadanie 2: \n')
    zadanie2()
    print('\nZadanie 3: \n')
    zadanie3()


