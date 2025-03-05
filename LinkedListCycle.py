class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(2)
node2=Node(2)
node3=Node(2)
node4=Node(2)

node1.next=node2
node2.next=node3
node3.next=node4    
node4.next=node2


# print("Node2 address" , id(node2))
# print("Node2 address stord in node1" , id(node1.next))
# print("checking both address are same" , id(node2)== id(node1.next))   

def hasCycle(head):
    if head==None:
        return False
    slow=head
    fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False


def traverseLinkedList(node):
    s = set()
    while node:
        if node in s:
            print(s)
            return True
        s.add(node)
        node=node.next
    print(s)
    return False

print(traverseLinkedList(node1))
print("================================")
print(hasCycle(node1))