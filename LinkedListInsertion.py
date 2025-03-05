class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(1)
node2=Node(5)
node3=Node(7)

node1.next=node2
node2.next=node3

currentnode=node1

# Print Linkedlist before insertion
def traverseLinkedList(node):
    while node:
        print(node.data)
        node=node.next

print("Before Insertion")
traverseLinkedList(node1)

def insertNode(first,newnode,position):
    if position==1:
        newnode.next=first
        return newnode
    if position<=0:
        print("Invalid Position")
        return first
    
    currentnode=first
    for _ in range(position-2):
        if currentnode.next==None:
            break
        currentnode=currentnode.next

    newnode.next=currentnode.next
    currentnode.next=newnode
    return first

newnode=Node(10)
node1=insertNode(node1,newnode,1)
print("After Insertion")
traverseLinkedList(node1)