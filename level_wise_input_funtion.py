def take_input_level_wise():
  q = queue.Queue()
  print('enter the root')
  root_data = int(input())
  if root_data == -1:
    return None
  root = Tree(root_data)
  q.put(root)
  while(q.empty() is not True):
    curr_node = q.get()
    print('enter the left child of ',curr_node.data)
    left_child_data = int(input())
    if left_child_data != -1:
      left_child = Tree(left_child_data)
      curr_node.left = left_child
      q.put(left_child)
    print('enter the right child of ',curr_node.data)
    right_child_data = int(input())
    if right_child_data != -1:
      right_child = Tree(right_child_data)
      curr_node.right = right_child
      q.put(right_child)
    return root

