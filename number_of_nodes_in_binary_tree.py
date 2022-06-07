
def number_of_nodes(root):
  if root == None:
    return 0
  left_ans = number_of_nodes(root.left)
  right_ans = number_of_nodes(root.right)
  total_nodes = 1 + left_ans + right_ans
  return total_nodes
