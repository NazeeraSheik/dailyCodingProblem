'''Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.'''
class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        
def checkIntersection(head1,head2):
    hs=set()
    while head1 is not None:
        hs.add(head1.data)
        head1=head1.next
    while head2 is not None:
        if(head2.data in hs):
            print(head2.data)
            break
        head2=head2.next

head1=Node(3)
head1.next=Node(7)
head1.next.next=Node(8)
head1.next.next.next=Node(10)

head2=Node(99)
head2.next=Node(1)
head2.next.next=Node(8)
head2.next.next.next=Node(10)

checkIntersection(head1,head2)
