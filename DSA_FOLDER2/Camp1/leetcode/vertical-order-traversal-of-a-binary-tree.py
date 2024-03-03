class Solution:
  def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    nodesLis = []
    nodesDic = collections.defaultdict(list)

    def backT(node: Optional[TreeNode], x: int, y: int) -> None:
      if not node:
        return
      nodesDic[x].append((-y, node.val))
      backT(node.left, x - 1, y - 1)
      backT(node.right, x + 1, y - 1)

    backT(root, 0, 0)

    for _, nodes in sorted(nodesDic.items(), key=lambda item: item[0]):
      nodesLis.append([val for _, val in sorted(nodes)])

    return nodesLis