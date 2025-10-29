"""
Full tree - every node has 0 or 2 children
Perfect tree - all leaf nodes are at the same level (last level us fully filled in)
Complete tree - all levels are filled in except the last level, and the last level is
                filled in from left to right
Balanced tree - the height of the left and right subtree of any node differ by not more
                than 1

Binary search tree - every node to the left of a parent node is always less than
                     the parent, greater nodes go to the right; always counting from the
                     top level node (root) when adding new nodes; no duplicatesd values
                     are allowed in a BST

Lookup, insert, remove:
Heigh of the tree (number of levels) is approximately O(log n).
O(n) - Omikron (worst case): if the tree never forks (is a linked list)
Θ(log n), Ω(log n) - Omega (best case) and Theta (average case):
                     remove half of the tree from search at each step (divide & conquer)
Normally, we assume it forks and treat it as O(log n).
"""


class BinaryNode:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = BinaryNode(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while True:
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    else:
                        temp = temp.left
                elif new_node.value > temp.value:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right
                else:
                    return False
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __recursive_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            next_node = current_node.left
        if value > current_node.value:
            next_node = current_node.right
        return self.__recursive_contains(next_node, value)

    def recursive_contains(self, value):
        return self.__recursive_contains(self.root, value)

    def __recursive_insert(self, current_node, value):
        if current_node is None:
            return BinaryNode(value)
        if value < current_node.value:
            current_node.left = self.__recursive_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__recursive_insert(current_node.right, value)
        return current_node

    def recursive_insert(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        self.__recursive_insert(self.root, value)

    def __delete_node(self, current_node, value):
        """
        - Deleting leaf node - just remove the node
        - Deleting node with one child - move the child (and its subtree) up to the
          node's position
        - Deleting node with two children - find the smallest node in the right subtree,
          copy it to in place of the node to delete, and delete the smallest node in the
          right subtree
        """
        if current_node is None:
            # Value to remove is not in the tree
            return None
        if value < current_node.value:
            # Traversing further left to find the node to delete
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            # Traversing further right to find the node to delete
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # Reached the node to delete, now we have 4 cases
            # Deleting leaf node
            if current_node.left is None and current_node.right is None:
                return None
            # Deleting node with only right child
            elif current_node.left is None:
                current_node = current_node.right
            # Deleting node with only left child
            elif current_node.right is None:
                current_node = current_node.left
            # Deleting node with both children
            else:
                subtree_min_value = self.min_value(current_node.right)
                current_node.value = subtree_min_value
                current_node.right = self.__delete_node(current_node.right, subtree_min_value)
        return current_node


    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def breadth_first_search(self):
        """
        Return a list of values in the tree layer by layer, left to right
        """
        current_node = self.root
        queue = [current_node]
        result = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result

    def depth_first_search_preorder(self):
        """
        Return a list of values in the tree (visit the node before visiting its children)
        - From root, go max to the left, storing all values
        - Go one step back and go to the right once, store the value
        - Repeat until all nodes are visited
        """
        results = []
        def traverse(node):
            results.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results

    def depth_first_search_postorder(self):
        """
        Return a list of values in the tree (visit the node only after visiting its children)
        """
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        return results

    def depth_first_search_inorder(self):
        """
        Find the leftmost node in the tree, visits that node, and subsequently visits
        the parent of that node. Rhen go to the child on the right and find the next
        leftmost node in the tree to visit.

        Results are sorted in ascending order.
        """
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results
