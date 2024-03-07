class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextNode = None
        self.prevNode = None
      

# self.head - wskaźnik na pierwszy element listy o ile lista nie jest pusta, aby uzyskać wartość dla tego wskażnika 
# trzeba dodatkowo skorzystać z value (self.head.value)
# nextNode pozwala nam przejśc do kolejnego wskaźnika z listy
class List:

    def __init__(self):
        self.head = None
        self.tail = None
        print('/*inicjuje zmienne*/')
    
    def list_insert(self,key):
        #node = type('Node',(),{'value':key,'nextNode':None,'prevNode':None})
        node = Node(key)

        if self.head is None:          
            self.head = node
            self.tail = node

        else:
            node.nextNode = self.head
            self.head = node
            while node:
                self.tail = node
                node = node.nextNode
                


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
        pass

    def list_delete(self,key):
        node = self.head
        prev_node = None
        while node:
            if node.value == key:
                if prev_node:
                    prev_node.nextNode = node.nextNode
                else:
                    self.head = node.nextNode
                return
            prev_node = node
            node = node.nextNode

    def list_insert_before(self,key,before):
        pass
    
    def clear(self):
        return print('/*zwalnia pamięć*/')
    
    def test(self):
        print('\nTestowanie, funkcja poza tematem zadania:')
        print('Test Head:',self.head.value)
        print('Test Tail:',self.tail.value)

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
    L.list_insert_before(5,3)
    L.write()
    L.clear()
    L.write()
    L.test()

if __name__ == '__main__':
    print('Zadanie 1: \n')
    zadanie1()
    # print('\nZadanie 2: \n')

    # print('\nZadanie 3: \n')
    

