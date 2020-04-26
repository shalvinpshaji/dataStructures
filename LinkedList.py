class Node:
  def __init__(self,value=None):
    self.value = value
    self.next = None
class Linked:
  def __init__(self):
    self.head = Node()
    self.len=0
  def insert(self,value):
    self.len+=1
    if self.head.value==None:
      self.head.value=value
    else:
      temp = self.head
      while temp.next!=None:
        temp = temp.next
      new = Node(value)
      temp.next = new
  def print(self):
    temp = self.head
    while temp!=None:
      print(temp.value)
      temp = temp.next
  def remove(self,pos=None):
    temp = self.head
    if pos is None:
      self.len-=1
      if temp.next == None:
        temp.value =None
        temp.next = None
      else:
        while temp.next.next!=None:
          temp = temp.next
        temp.next = None
    else:
      if pos<0:
        pos = self.len-pos
      if pos==0:
        self.head = self.head.next
        self.len-=1
      elif pos<self.len:
        i=0
        while i<pos-1:
          temp = temp.next
          i+=1
        
        temp.next = temp.next.next
        self.len-=1
      else:
        print("Index out of range!!")
  def print_with_index(self):
    temp = self.head
    i=0
    while temp!=None:
      print(f"{i} : {temp.value}")
      temp = temp.next
      i+=1


l = Linked()
for i  in range(20):
  l.insert(i)
l.print_with_index()
l.remove(20)
l.print_with_index()
l.remove(20)
l.print_with_index()
l.remove(6)
l.print_with_index()
