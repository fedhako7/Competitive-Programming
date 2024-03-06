"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        

            roots = defaultdict(list)
            def populate(root, depth):
                if not root:
                    return

                roots[depth].append(root)
                populate(root.left, depth + 1)
                populate(root.right, depth + 1)

            populate(root, 0)

            for depth in roots:
                currRoots = roots[depth]
                L = len(currRoots)
                currRoots[L - 1].next = None

                for idx in range(L - 1):
                    currRoots[idx].next = currRoots[idx + 1]


            return root













