#a function that takes in integer m and and returns mth value from the end of a linked list

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





linked_list = LinkedList()

linked_list.append("g")
linked_list.append("f")
linked_list.append("e")
linked_list.append("d")
linked_list.append("c")
linked_list.append("b")
linked_list.append("a")

linked_list.print_list()

linked_list.remove(0)
linked_list.print_list()

linked_list.append("a")
linked_list.print_list()

linked_list.remove(2)
linked_list.print_list()

linked_list.insert("i", 2)
linked_list.print_list()
m = int(input("Enter the number of position from the end of the list: "))
value = mthvalue(linked_list, m)
print("value is: " + str(value))