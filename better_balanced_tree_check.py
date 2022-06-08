def is_balanced_better_version(root):
  if root == None:
    return 0 ,True
  left_height,isleft_balanced = is_balanced_better_version(root.left)
  right_height,isright_balanced = is_balanced_better_version(root.right)
  height = 1 + max(left_height,right_height)
  if abs(left_height - right_height) > 1:
    return height , False
  if isleft_balanced == True and isright_balanced == True:
    return height , True
  else:
    return height , False

def is_binary_tree_balanced(root):
  height , is_balanced_for_tree = is_balanced_better_version(root)
  if is_balanced_for_tree == True:
    return True
  else:
    return False
