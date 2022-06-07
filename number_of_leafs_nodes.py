def number_of_leafs_node(root):
  if root == None:
    return 0
  if root.left == None and root.right == None:
    return 1 
  left_ans = number_of_leafs_node(root.left)
  right_ans =  number_of_leafs_node(root.right)
  ans = left_ans + right_ans
  return ans

