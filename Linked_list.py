class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)    


    def inset_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.insert_at_start(data)
            return 

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1



    def print(self):
        itr  =  self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr) 

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
           


root = Linkedlist()
root.insert_at_start(5)
root.insert_at_start(2) 
root.insert_at_end(5)
root.insert_at_end(10)
root.inset_at(2,6)
root.inset_at(1,7)
root.print()     

root.remove_at(2)

root.print()     
print("length of Linkedlist:",root.get_length())