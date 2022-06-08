def remove_leaf_nodes(root):
  if root == None:
    return None
  if root.left == None and root.right == None:
    return None
  left_ans = remove_leaf_nodes(root.left)
  right_ans = remove_leaf_nodes(root.right)
  root.left = left_ans
  root.right = right_ans
  return root 
  
