class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        q = sorted((time, i) for i, time in enumerate(queries))

        ans = [0] * len(queries)

        server_count = {}

        left = 0
        right = 0
        m = len(logs)

        for time, idx in q:
            while right < m and logs[right][1] <= time:
                server = logs[right][0]

                server_count[server] = server_count.get(server, 0) + 1

                right += 1

            # Remove logs outside the lower boundary
            while left < right and logs[left][1] < time - x:
                server = logs[left][0]

                server_count[server] -= 1

                if server_count[server] == 0:
                    del server_count[server]

                left += 1

            ans[idx] = n - len(server_count)

        return ans