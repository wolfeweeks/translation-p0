import sys
import os
import stat
import node


def printPreorder(root, file):
    if root:
        root.write(file)
        printPreorder(root.left, file)
        printPreorder(root.right, file)


def printInorder(root, file):
    if root:
        printInorder(root.left, file)
        root.write(file)
        printInorder(root.right, file)


def printPostorder(root, file):
    if root:
        printPostorder(root.left, file)
        printPostorder(root.right, file)
        root.write(file)


def buildTree():
    firstWord = True
    root = None

    # if user entered filename as argument
    if len(sys.argv) == 2:
        filename = sys.argv[-1] + '.cs4280'
        if not os.path.exists(filename):
            print('the file \'' + filename + '\' does not exist')
            sys.exit()

        f = open(filename, 'r')
        for line in f:
            line = line.rstrip('\n')  # remove any newlines
            words = line.split()  # split up any words by whitespace
            for word in words:
                if firstWord:
                    # if firstword, create the root node
                    root = node.Node(len(word), [word], 0)
                    firstWord = False
                else:
                    root.insert(word)

    # if user does not pass file as command line argument
    else:
        # code to check if stdin is redirected or not found at link below
        # https://stackoverflow.com/questions/13442574/how-do-i-determine-if-sys-stdin-is-redirected-from-a-file-vs-piped-from-another
        mode = os.fstat(sys.stdin.fileno()).st_mode
        # if stdin is from a redirect
        if stat.S_ISREG(mode):
            for line in sys.stdin:
                line = line.rstrip('\n')  # remove any newlines
                words = line.split()  # split up any words by whitespace
                for word in words:
                    if firstWord:
                        # if firstword, create the root node
                        root = node.Node(len(word), [word], 0)
                        firstWord = False
                    else:
                        root.insert(word)
        # if no file redirected
        else:
            try:
                print(
                    'Enter words and lines and press Ctrl-D (Ctrl-Z on Windows) when finished')
                while True:
                    line = raw_input()  # get user input
                    line = line.rstrip('\n')  # remove any newlines
                    words = line.split()  # split up any words by whitespace
                    for word in words:
                        if firstWord:
                            # if firstword, create the root node
                            root = node.Node(len(word), [word], 0)
                            firstWord = False
                        else:
                            root.insert(word)
            except EOFError:
                pass

    return root
