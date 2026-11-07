import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        current_time = 0

        for j, task in enumerate(tasks):

            current_time = max(current_time, j)

            while busy and busy[0][0] <= current_time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            if not available:
                current_time = busy[0][0]

                while busy and busy[0][0] == current_time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            weight, idx = heapq.heappop(available)

            ans.append(idx)

            heapq.heappush(
                busy,
                (current_time + task, weight, idx)
            )

        return ans
