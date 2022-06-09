
def build_tree_from_inorder_preorder(inorder,preorder,n):
  if len(inorder) == 0 or len(preorder) ==0:
    return 
  root = Tree(preorder[0])
  mid = -1
  for i in range(0,len(inorder)):
    if inorder[i] == preorder[0]:
      mid = i
      break
  if mid == -1:
    return None
      
  root.left =  build_tree_from_inorder_preorder(inorder[0:mid+1],preorder[1:mid+1],n)
  root.right =  build_tree_from_inorder_preorder(inorder[mid+1:],preorder[mid+1:],n)
  return root
