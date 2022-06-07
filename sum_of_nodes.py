def sum_of_nodes(root):
  if root == None:
    return 0
  left_ans = sum_of_nodes(root.left)
  right_ans = sum_of_nodes(root.right)
  sum = root.data + left_ans + right_ans
  return sum
