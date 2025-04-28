from typing import List
from collections import defaultdict


"""
TIME: 727ms (Beats 5.00%)
NOTE: This is union find without any optimizations (and also having the parent data structure as a dictionary and not an array)

TIME: 49ms (Beats 22.90%)
NOTE: I added union by rank and path compression optimizations to the union find algorithm and just look at the result FUCK ME I AM GOATED.
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = defaultdict(str)
        rank = defaultdict(int)

        def find(mail: str):
            if parent[mail] != "" and parent[mail] != mail:
                parent[mail] = find(parent[mail])
                return parent[mail]
            return mail

        def union(name: str, mail: str):
            name_root = find(name)
            mail_root = find(mail)

            if rank[name_root] > rank[mail_root]:
                parent[mail_root] = name_root
            elif rank[name_root] < rank[mail_root]:
                parent[name_root] = mail_root
            else:
                parent[mail_root] = name_root
                rank[name_root] += 1

        for i, info in enumerate(accounts):
            name = i
            mails = info[1:]

            for mail in mails:
                union(name, mail)

        merged_accounts = [[] for _ in range(n)]
        for i, info in enumerate(accounts):
            name_root = find(i)
            merged_accounts[name_root].extend(info[1:])

        return [
            [accounts[i][0], *sorted(set(mails))]
            for i, mails in enumerate(merged_accounts)
            if mails != []
        ]


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            [
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ]
        ),
        # (
        #     [
        #         ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        #         ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
        #         ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
        #         ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
        #         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        #     ]
        # ),
    ]

    for accounts in q:
        for row in accounts:
            print(row)
        print()
        answer = solution.accountsMerge(accounts)
        print("answer: ", answer)
        print("=====================")
        print()
