class Node:
    def __init__(self, length, strings, depth):
        self.length = length
        self.strings = strings
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, string):
        if self.length == len(string):
            if self.strings == None:
                self.strings = []
            if not string in self.strings:
                self.strings.append(string)
        elif len(string) < self.length:
            if self.left == None:
                self.left = Node(len(string), [string], self.depth + 1)
            else:
                self.left.insert(string)
        else:
            if self.right == None:
                self.right = Node(len(string), [string], self.depth + 1)
            else:
                self.right.insert(string)

    def write(self, file):
        line = ''
        for i in range(self.depth):
            line += '  '
        line += str(self.length) + ': '
        for string in self.strings:
            line += string + ' '
        file.write(line + '\n')
