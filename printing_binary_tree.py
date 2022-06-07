class Tree:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None



def print_tree(root):
  if root == None:
    return
  print(root.data,end= ": ")
  if root.left != None:
    print("l:",root.left.data,end = ', ')
  if root.right != None:
    print("r:",root.right.data,end ='')
  print()
  print_tree(root.left)
  print_tree(root.right)
  
  
  
  

t1 = Tree(1)
t2 = Tree(2)
t3 = Tree(3)
t4 = Tree(33)
t5 = Tree(304)
t6 = Tree(306666)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t5.left = t6
print_tree(t1)

