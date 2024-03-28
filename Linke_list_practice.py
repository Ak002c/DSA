class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head = node

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_end(self,data):
        if self.head == None:
            self.insert_at_start(data)
            return 

        itr = self.head
        while itr.next:
              itr = itr.next
        itr.next = Node(data)   

    def insert_at(self,index,data):
        if index < 0 or index >= self.length():
            raise Exception("index outoff range")  

        if index == 0:
            self.insert_at_start(data)

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                return
            count += 1
            itr = itr.next

    def delete(self,index):

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            break  
        itr = itr.next
        count += 1      


    def print(self):
        itr = self.head
        llstr = ''

        while itr:
            suffix = ''
            if itr.next :
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

root = linkedlist()
root.insert_at_start(1)
# root.insert_at_start(2)
root.insert_at_end(2)
root.insert_at(0,5)
root.insert_at(1,9)
root.print()    
root.delete(1)
root.print()    
print("length of linkedlist:",root.length())


