
def is_node_present(root,x):
  if root == None:
    return Fasle
  if root.data == x:
    return True
  l_ans = is_node_present(root.left,x)
  r_ans = is_node_present(root.right,x)
  return l_ans or r_ans
  
