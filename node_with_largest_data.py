def node_with_greatest_data(root):
  if root == None:
    return -1
  left_ans = node_with_greatest_data(root.left)
  right_ans = node_with_greatest_data(root.right)
  largest = max(root.data,left_ans,right_ans)
  return largest

