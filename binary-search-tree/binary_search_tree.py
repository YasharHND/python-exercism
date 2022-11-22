class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree = TreeNode(tree_data[0], None, None)
        for data in tree_data[1:]:
            node = self.tree
            while True:
                if data <= node.data:
                    if node.left is None:
                        node.left = TreeNode(data, None, None)
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = TreeNode(data, None, None)
                        break
                    else:
                        node = node.right

    def data(self):
        return self.tree

    def sorted_data(self):
        out = []
        remaining_nodes = [self.tree]
        while len(remaining_nodes) > 0:
            node = remaining_nodes.pop()
            insert_sorted(out, node.data)
            if node.left is not None:
                remaining_nodes.append(node.left)
            if node.right is not None:
                remaining_nodes.append(node.right)
        return out


def insert_sorted(sorted_list, data):
    for idx, n in enumerate(sorted_list):
        if data <= n:
            sorted_list.insert(idx, data)
            break
    else:
        sorted_list.append(data)
