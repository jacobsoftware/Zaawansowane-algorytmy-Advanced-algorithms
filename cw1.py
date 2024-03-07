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
    
    def test(self):
        print('\nTestowanie, funkcja spoza tematu zadania:')
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
    #L.test()

if __name__ == '__main__':
    print('Zadanie 1: \n')
    zadanie1()
    # print('\nZadanie 2: \n')

    # print('\nZadanie 3: \n')


    

