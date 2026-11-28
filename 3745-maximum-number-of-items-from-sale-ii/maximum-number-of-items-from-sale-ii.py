from collections import defaultdict


class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        cnt_factor = [0] * (n + 1)
        min_price = float("inf")

        for factor, price in items:
            cnt_factor[factor] += 1
            if price < min_price:
                min_price = price

        cnt_multi = [0] * (n + 1)
        price_to_bonus = defaultdict(int)

        for factor, price in items:
            if price >= 2 * min_price:
                continue
            if cnt_multi[factor] == 0:
                total_multi = 0
                for mult in range(factor, n + 1, factor):
                    total_multi += cnt_factor[mult]
                cnt_multi[factor] = total_multi

            free_targets = cnt_multi[factor] - 1
            if free_targets > 0:
                price_to_bonus[price] += free_targets

        ans = 0
        for price in sorted(price_to_bonus):
            if budget < price:
                break
            available = price_to_bonus[price]
            take = min(available, budget // price)
            budget -= take * price
            ans += take * 2

        ans += budget // min_price
        return ans
