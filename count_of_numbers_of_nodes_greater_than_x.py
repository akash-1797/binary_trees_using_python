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

