# Floy'd cycle detection / Hare-tortoise algorithm is a pointer algorithm that uses only two pointers, moving through the sequence at different pace. One is twice as faster than the other

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def find_cycle(head):
    if head == None :
        return False 


    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next != None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer : return True 
    
    return False 

def main():
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(0)
    head.next.next.next.next = Node(-4)

    #adding loop 
    temp = head 

    while temp.next != None:
        temp = temp.next
    temp.next = head 
    
    res = find_cycle(head)
    print(res)



if __name__ == '__main__':
    main()
