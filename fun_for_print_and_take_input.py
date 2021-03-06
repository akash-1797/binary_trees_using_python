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
  
  
def take_input():
  root_data = int(input())
  if root_data == -1:
    return 
  root = Tree(root_data)
  left_tree = take_input()
  right_tree = take_input()
  root.left = left_tree
  root.right = right_tree
  return root
  
root = take_input()
print_tree(root)


