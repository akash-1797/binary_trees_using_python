
def height_of_binary_tree(root):
  if root == None:
    return 0
  left_height = height_of_binary_tree(root.left)
  right_height = height_of_binary_tree(root.right)
  ans = 1 + max(left_height,right_height)
  return ans 

def is_balanced(root):
  if root == None:
    return True
  left_height =  height_of_binary_tree(root.left)
  right_height =  height_of_binary_tree(root.right)
  if abs(left_height -  right_height) > 1:
    return False
  left_ans = is_balanced(root.left)
  right_ans = is_balanced(root.right)
  if left_ans == True and right_ans == True:
    return True
  else:
    return False
