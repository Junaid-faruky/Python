class Node:
    def _init_(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    print("Right to Left")
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()
 
def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    # left to right link 
    # 11 --> 22 --> 33 --> 44 --> None  
    # newBlock = 44  
    # tail = 33 
    tail.next = newBlock 
 
    # right to left link 
    newBlock.prev = tail 
    return head
 
def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    # 11 --> 22 --> 33 --> None 
    # newBlock = 10
    # head = 11 
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock
 
def insertAtSpecificPosition(head, val, position):
    newBlock = Node(val)
    if head == None:
        return newBlock
 
    index = 1 
    curr = head 
 
    while index != position - 1:
        index += 1 
        curr = curr.next 
    nextNode = curr.next 
    # 11 --> 22 --> 33 --> 44 --> 55 --> 66 --> None 
    #  1      2     3       4      5      6 
 
    # (4, 12)
    # curr = 33 
    # newBlock = 12 
    # nextNode = 44 
 
    newBlock.next = nextNode 
    nextNode.prev = newBlock 
 
    # 12 --> 44
    # 12 <-- 44 
 
    curr.next = newBlock 
    newBlock.prev = curr 
 
    # 33 --> 12 
    # 33 <-- 12 
 
    return head
 
def deleteTailNodeInDoublyLinkedList(head):
    if head == None or head.next == None:
        return None 
    # 11 --> None 
    # 11 --> 22 --> 33 --> 44 --> None
    # curr = head 
    # previous = None 
    curr, previous = head, None
    while curr.next != None:
        previous = curr 
        curr = curr.next 
    # previous = 33 
    # curr = 44 
    previous.next = None 
    curr.prev = None 
    return head 
 
def deleteHeadNodeInDoublyLinkedList(head):
    if head == None or head.next == None:
        return None 
    # 11 --> 22 --> 33 --> 44 --> None
    secondNode = head.next 
    head.next = None 
    secondNode.prev = None 
    return secondNode 
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInDoublyLinkedList(head)
    # 11 --> 22 --> 33 --> 44 --> None
    # 1       2      3      4 
 
    # position = 3 
    # curr = 22 
    # nodeToBeDeleted = 33 
    # nextNode = 44
 
    curr = head 
    index = 1 
 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    nodeToBeDeleted = curr.next 
    nextNode = nodeToBeDeleted.next 
    curr.next = nextNode 
    nextNode.prev = curr 
    return head
 
l = [11, 22, 33, 44, 55, 66, 77]
head = None 
for ele in l:
    #head = addNodeAtTailOfLinkedList(head, ele)
    head = addNodeAtHeadOfLinkedList(head, ele)
 
printLeftToRightManner(head)
printRightToLeftManner(head)   
 
#head = insertAtSpecificPosition(head, 12222, 3)
head = deleteNodeAtSpecificPosition(head, 4)
 
printLeftToRightManner(head)
printRightToLeftManner(head)
 
# Left to Right
# 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 11 --> 
# Right to Left
# 11 --> 22 --> 33 --> 44 --> 55 --> 66 --> 77 --> 
# Left to Right
# 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 
# Right to Left
# 22 --> 33 --> 44 --> 55 --> 66 --> 77 -->
