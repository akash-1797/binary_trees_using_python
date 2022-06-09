def  build_tree_from_inorder_postorder(inorder,postorder,n):
  if len(inorder) == 0 or len(postorder) ==0:
      return
  root = Tree(postorder[-1])
  mid  = -1
  for i in range(0,len(inorder)):
    if inorder[i] == postorder[-1]:
      mid  = i
      break
  if mid  == -1:
    return None
  root.left = build_tree_from_inorder_postorder(inorder[0:mid],postorder[0:mid],n)
  root.right = build_tree_from_inorder_postorder(inorder[mid+1:],postorder[mid:-1],n)
  return root
