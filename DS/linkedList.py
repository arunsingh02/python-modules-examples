class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node

    def set_data(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
        return self.data


class Linked_list():
    def __init__(self, head = None):
        #Node.__init__(self)
        self.head = head

    def insert_at_end(self, data):
        new_node = Node(data)
        next_node = new_node.get

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node
        print(self.head)

    def size(self):
        current = self.head
        c = 0
        while current:
            c += 1
            print(current.get_data())
            current = current.get_next_node()
        return c

    def search(self, data):
        current = self.head
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next_node()

        if found:
            print('founded data %s'% data)
        else:
            raise ValueError('not found')

    def delete(self, data):
        current = self.head
        found = False
        previous = None
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next_node()
        if found:
            previous.set_next_node(current.get_next_node())
        if previous == None:
            self.head = current.get_next_node()
        return

    def insert_in_between(self, sdata, data):
        current = self.head
        found = False
        previous = None
        while current and found == False:
            if current.get_data() == sdata:
                found = True
            else:
                previous = current
                current  = current.get_next_node()
        print('FOUND : ', found)
        if found:
            new_node = Node(data, current)
            new_node.set_next_node(current.get_next_node())
        else:
            pass

    def reverse(self):
        previous = None
        current = self.head
        while current != None:
            next_node = current.get_next_node()
            current.set_next_node(previous)
            previous = current
            current = next_node
        self.head = previous


if __name__ == '__main__':
    ll = Linked_list()
    ll.insert(123)
    #print ll.size()
    ll.insert(233)
    ll.insert('Arun')
    ll.insert('Ravi')
    #print ll.size()
    ll.search(123)
    #print ll
    #ll.delete(123)
    #print ll.size()
    #ll.insert_in_between(123, 456)
    print(ll.size())
    ll.reverse()
    print(ll.size())