import sys
import tree


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('too many command line arguments')
        sys.exit()

    if len(sys.argv) == 2:
        filename = sys.argv[-1]  # get filename if passed as command line arg
    else:
        filename = 'outP0'

    root = tree.buildTree()

    # open respective files in write mode
    preorderFile = open(filename + '.preorder', 'w')
    inorderFile = open(filename + '.inorder', 'w')
    postorderFile = open(filename + '.postorder', 'w')

    # write traversals to their respective files
    tree.printPreorder(root, preorderFile)
    tree.printInorder(root, inorderFile)
    tree.printPostorder(root, postorderFile)

    preorderFile.close()
    inorderFile.close()
    postorderFile.close()
