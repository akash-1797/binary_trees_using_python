def height_of_binary_tree(root):
  if root == None:
    return 0
  left_height = height_of_binary_tree(root.left)
  right_height = height_of_binary_tree(root.right)
  ans = 1 + max(left_height,right_height)
  return ans 
