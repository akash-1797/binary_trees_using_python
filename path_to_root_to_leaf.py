
def path_finder_helper(root,string,path):
  if root == None:
    return 
  string = string + str(root.data)
  path_finder_helper(root.left,string + " ",path)
  path_finder_helper(root.right,string + " ",path)
  if root.left == None and root.right == None:
    path.append(string)
    return 


def path_finder(root):
  if root == None:
    print(" ")
    return 
  path = []
  path_finder_helper(root,' ',path)
  for i in range(0,len(path)):
    print(path[i],end =' ')
    print()
  return
