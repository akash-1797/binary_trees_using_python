def printLevelWise(root):
    if root == None:
        return 
    q = queue.Queue()
    q.put(root)
    while(not(q.empty())):
        curr_node = q.get()
        print(curr_node.data,end=':')
        if curr_node.left != None:
            print("L:",end = "")
            print(curr_node.left.data,end = "," )
            q.put(curr_node.left)
        else:
            print("L:-1",end=',')
        if curr_node.right != None:
            print("R:",end = "")
            print(curr_node.right.data,end = "" )
            q.put(curr_node.right)
        else:
            print("R:-1",end='')
        print()
        
