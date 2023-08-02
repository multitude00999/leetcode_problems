class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root

        # do bfs over tree to find p and q, keep storing parent of each node in par_dict
        queue = deque([root])
        par_dict = {root.val: root.val}
        val_parent = {}
        foundP, foundQ = False, False
        cnt = 0
        while len(queue):
            level_size = len(queue)
            for i in range(level_size):
                curr = queue.popleft()
                # val parent for storing parent of each value
                val_parent[curr.val] =  curr
                
                # check if P found
                if curr.val == p.val:
                    foundP = True
                
                if curr.val == q.val:
                    foundQ = True
                
                # break if both p and q are found
                if foundP and foundQ :
                    break
                

                if curr.left:
                    queue.append(curr.left)

                    # update parent of child
                    par_dict[curr.left.val] = curr.val
                if curr.right:
                    queue.append(curr.right)
                    # update parent of child
                    par_dict[curr.right.val] = curr.val

        # make a list of parents of p
        par_p = [p.val, par_dict[p.val]]
        curr = par_p[-1]
        while curr != root.val:
            curr = par_dict[curr]
            par_p.append(curr)

        # make a list of parents of q
        par_q = [q.val, par_dict[q.val]]
        curr = par_q[-1]

        # check if parent of q already in par_p
        if q.val in par_p:
            return q

        # keep checking if parent of q in p until root node
        while curr != root.val:
            if curr in par_p:
                return val_parent[curr]
            curr = par_dict[curr]
            par_q.append(curr)

        return root