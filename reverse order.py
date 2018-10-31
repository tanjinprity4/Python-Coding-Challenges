#given singly linkedList, return another linked list
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# -> [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]

class Node():
  def __init__(self, value = None, nxt = None):
    self.value = value
    self.nxt = nxt 

class LinkedList():

  def __init__(self):
    self.head = None

  def append(self, value):
    new_node = Node(value, self.head)
    self.head = new_node

  def insert(self, value, pos):
    if pos == 0:
      self.append(value)
      return
    prev = self.head
    node = self.head.nxt
    for i in range(pos-1):
      prev = node
      node = node.nxt
    new_node = Node(value, node)
    prev.nxt = new_node

  def remove(self, pos):
    if pos == 0:
      node = self.head
      self.head = self.head.nxt
      del node
      return
    prev = self.head
    node = self.head.nxt
    for i in range(pos-1):
      prev = node
      node = node.nxt
    prev.nxt = node.nxt
    del node

  def print_list(self):
    to_print = "["
    node = self.head
    while node.nxt is not None:
        to_print += str(node.value) + ", "
        node = node.nxt
    to_print += str(node.value) + "]"
    print(to_print)

def mthvalue(linkedList, m):
  node = linkedList.head
  count = 0
  while node is not None:
    node = node.nxt
    count+=1
  pos = count - m
  node = linkedList.head
  for i in range(0,pos):
    node = node.nxt
  mth_value = node.value
  return mth_value

def reverseOrder(linkedList):
    node = linkedList.head
    node2 = linked_list.head.nxt
    while node.nxt and node2.nxt is not None:
        lnode = linkedList.head
        lnode2 = linkedList.head.nxt
        last_node = lnode2.nxt
        count = 1
        while lnode2.nxt is not None:
          lnode = lnode2
          lnode2 = last_node
          if last_node is not None:
            last_node = last_node.nxt
          count+=1
        new_node = lnode2
        lnode.nxt = None
        
        node.nxt = new_node
        if new_node is not None:
          new_node.nxt = node2
        node= node2
        node2 = node.nxt
    linked_list.print_list()

    return linked_list
    




linked_list = LinkedList()

linked_list.append(0)
linked_list.append(9)
linked_list.append(8)
linked_list.append(7)
linked_list.append(6)
linked_list.append(5)
linked_list.append(4)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)
linked_list.print_list()
reverseOrder(linked_list)


# linked_list.remove(0)
# linked_list.print_list()

# linked_list.append("a")
# linked_list.print_list()

# linked_list.remove(2)
# linked_list.print_list()

# linked_list.insert("i", 2)
# linked_list.print_list()
# m = int(input("Enter the number of position from the end of the list: "))
# value = mthvalue(linked_list, m)
# print("value is: " + str(value))

