class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(1)
node2=Node(5)
node3=Node(7)

node1.next=node2
node2.next=node3    


def traverseLinkedList(node):
    while node:
        print(node.data)
        node=node.next
    
print("Before Deletion")
traverseLinkedList(node1)       

def deleteNode(first,deletenode):
    if first==deletenode:
        return first.next
    
    currentnode=first
    while currentnode.next and currentnode.next!=deletenode:
        currentnode=currentnode.next
    
    currentnode.next=currentnode.next.next
    return first

node1=deleteNode(node1,node1)
    
print("After Deletion")
traverseLinkedList(node1)   
