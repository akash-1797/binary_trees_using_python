class Tree:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

#----------------------------------------------------#

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

#----------------------------------------------------#
  
  
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

#----------------------------------------------------#


def number_of_nodes(root):
  if root == None:
    return 0
  left_ans = number_of_nodes(root.left)
  right_ans = number_of_nodes(root.right)
  total_nodes = 1 + left_ans + right_ans
  return total_nodes

#----------------------------------------------------#
  
def sum_of_nodes(root):
  if root == None:
    return 0
  left_ans = sum_of_nodes(root.left)
  right_ans = sum_of_nodes(root.right)
  sum = root.data + left_ans + right_ans
  return sum

#----------------------------------------------------#

def node_with_greatest_data(root):
  if root == None:
    return -1
  left_ans = node_with_greatest_data(root.left)
  right_ans = node_with_greatest_data(root.right)
  largest = max(root.data,left_ans,right_ans)
  return largest

#----------------------------------------------------#
  
def number_of_nodes_greater_than_x(root,x):
  count = 0
  if root == None:
    return 0
  left_ans = number_of_nodes_greater_than_x(root.left,x)
  right_ans = number_of_nodes_greater_than_x(root.right,x)
  if root.data > x:
    count = count +1
  final_answer = count + left_ans + right_ans
  return final_answer

#----------------------------------------------------#

def height_of_binary_tree(root):
  if root == None:
    return 0
  left_height = height_of_binary_tree(root.left)
  right_height = height_of_binary_tree(root.right)
  ans = 1 + max(left_height,right_height)
  return ans 
#----------------------------------------------------#

def number_of_leafs_node(root):
  if root == None:
    return 0
  if root.left == None and root.right == None:
    return 1 
  left_ans = number_of_leafs_node(root.left)
  right_ans =  number_of_leafs_node(root.right)
  ans = left_ans + right_ans
  return ans
#----------------------------------------------------#
  

def print_nodes_at_depth_k(root,k):
  if root == None:
    return 
  if k == 0 :
    print(root.data,end = ' ')
    return 
  print_nodes_at_depth_k(root.left,k-1)
  print_nodes_at_depth_k(root.right,k-1)

#----------------------------------------------------#

def print_nodes_at_depth_k_version_2(root,k,d = 0):
  if root == None:
    return 
  if k == d:
    print(root.data,end= ' ')
    return 
  print_nodes_at_depth_k_version_2(root.left,k,d+1)
  print_nodes_at_depth_k_version_2(root.right,k,d+1)

#----------------------------------------------------#

def is_node_present(root,x):
  if root == None:
    return Fasle
  if root.data == x:
    return True
  l_ans = is_node_present(root.left,x)
  r_ans = is_node_present(root.right,x)
  return l_ans or r_ans

#----------------------------------------------------#

def nodes_without_siblings(root):
  if root == None:
    return 
  if root.left != None and root.right != None:
    nodes_without_siblings(root.left)
    nodes_without_siblings(root.right)
  elif root.left != None:
    print(root.left.data,end = ' ')
    nodes_without_siblings(root.left)
  elif root.right != None:
    print(root.right.data,end = ' ')
    nodes_without_siblings(root.right)

#----------------------------------------------------#
    
    
  
  
root = take_input()
print_tree(root)
print(nodes_without_siblings(root))

