def mirror_image_of_binary_tree(root):
  if root == None:
    return 
  mirror_image_of_binary_tree(root.left)
  mirror_image_of_binary_tree(root.right)
  temp = root.left
  root.left = root.right
  root.right = temp
  return root
