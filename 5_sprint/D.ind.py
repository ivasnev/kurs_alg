def solution(root1, root2):
    if (root1 == None and root2 == None):
        return True
    elif (root1 != None and root2 == None):
        return False
    elif (root1 == None and root2 != None):
        return False
    else:
        if (root1.value == root2.value and
                solution(root1.left, root2.left)
                and solution(root1.right, root2.right)):
            return True
        else:
            return False
