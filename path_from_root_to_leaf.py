
def print_all_path_from_root_leaf(root,stack):
  if root == None:
    return 
  stack.append(root.data)
  print_all_path_from_root_leaf(root.left,stack)
  
  if root.left == None and root.right == None:
    for i in range(len(stack)):
      print(str(stack[i]),end = " ")
    print()
  print_all_path_from_root_leaf(root.right,stack)
  stack.pop()
  return 

