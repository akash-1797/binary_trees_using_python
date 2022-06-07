
def print_nodes_at_depth_k(root,k):
  if root == None:
    return 
  if k == 0 :
    print(root.data,end = ' ')
    return 
  print_nodes_at_depth_k(root.left,k-1)
  print_nodes_at_depth_k(root.right,k-1)

def print_nodes_at_depth_k_version_2(root,k,d = 0):
  if root == None:
    return 
  if k == d:
    print(root.data,end= ' ')
    return 
  print_nodes_at_depth_k_version_2(root.left,k,d+1)
  print_nodes_at_depth_k_version_2(root.right,k,d+1)
