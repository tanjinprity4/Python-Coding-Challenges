#The next challenge is to remove all items in a linked list whose values are greater than 100. 

class Node():
  def __init__(self, val = None, nxt = None):
    self.value = val
    self.nxt = nxt

class LinkedList():
  def __init__(self):
    self.head = None

  def append(self, value):
    new_node = Node(value, self.head)
    self.head = new_node

  def remove(self):
    node = self.head
    while self.head.value > 100:
      self.head = self.head.nxt
      del node
      node = self.head
    
    current = self.head.nxt
    while current.nxt is not None:
      if current.value > 100:
        node.nxt = current.nxt
        del current
        current = node.nxt
      else:
        node = current
        current = current.nxt
    if current.nxt == None and current.value > 100:
      node.nxt = None
      del current
  
  def print_list(self):
    to_print = ""
    current = self.head
    while current.nxt is not None:
      to_print += "| " + str(current.value) + " | -> "
      current = current.nxt
    to_print += "| " + str(current.value) + " |"
    print(to_print)

linked_list = LinkedList()
linked_list.append(122)
linked_list.append(120)
linked_list.append(30)
linked_list.append(190)
linked_list.append(150)
linked_list.append(25)
linked_list.append(132)
linked_list.append(170)
linked_list.append(123)
linked_list.append(12)
print("New list: ")
linked_list.print_list()


linked_list.remove()
print("Edited list: ")
linked_list.print_list()
print()

linked_list.append(52)
linked_list.append(180)
print("New list: ")
linked_list.print_list()

linked_list.remove()
print("Edited list: ")
linked_list.print_list()
