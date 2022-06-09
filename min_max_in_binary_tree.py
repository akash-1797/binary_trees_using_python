
def maximum_at_binary_tree(root):
  if root  == None:
    return float('-inf')
  return max(root.data,max(maximum_at_binary_tree(root.left),maximum_at_binary_tree(root.right)))
def minimum_at_binary_tree(root):
  if root == None:
    return float('inf')
  return(min(root.data,min( minimum_at_binary_tree(root.left), minimum_at_binary_tree(root.right))))


def minimum_and_maximum_binary_tree(root):
  min = minimum_at_binary_tree(root)
  max=  maximum_at_binary_tree(root)
  return max,min
