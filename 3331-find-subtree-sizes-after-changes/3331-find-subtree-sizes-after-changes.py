class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]

        last = {}

        def dfs(node):

            char = s[node]

            previous = last.get(char)

            last[char] = node

            for child in children[node]:

                if char in last:
                    new_parent[child] = last.get(s[child], new_parent[child])

                dfs(child)

            if previous is None:
                del last[char]
            else:
                last[char] = previous

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [1] * n

        def calculate(node):

            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer