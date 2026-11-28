class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        min_price = min(p for _, p in items)

        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1

        multiples = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] == 0:
                continue
            for m in range(f, max_factor + 1, f):
                multiples[f] += freq[m]

        deals_by_price = defaultdict(int)
        for f, price in items:
            if price < 2 * min_price:
                deals_by_price[price] += multiples[f] - 1

        total = 0
        for price in sorted(deals_by_price):
            count = min(deals_by_price[price], budget // price)
            total += 2 * count
            budget -= count * price
            if budget == 0:
                return total

        total += budget // min_price
        return total