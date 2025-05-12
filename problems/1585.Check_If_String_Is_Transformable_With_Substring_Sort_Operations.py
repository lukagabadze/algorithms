class Solution(object):
    def isTransformable(self, s: str, t: str) -> bool:
        n = len(s)

        # source_dist_map = [[[-1] * 10] for _ in range(n)]
        target_dist_map = [[[-1, -1] for _ in range(10)] for _ in range(n)]

        for i in range(n):
            c = int(t[i])
            for j in range(10):
                if c == j:
                    target_dist_map[i][j][0] = 0
                elif i > 0 and target_dist_map[i - 1][j][0] != -1:
                    target_dist_map[i][j][0] = target_dist_map[i - 1][j][0] + 1

        for i in reversed(range(n)):
            c = int(t[i])
            for j in range(10):
                if c == j:
                    target_dist_map[i][j][1] = 0
                elif i < n - 1 and target_dist_map[i + 1][j][1] != -1:
                    target_dist_map[i][j][1] = target_dist_map[i + 1][j][1] + 1

        # print("target_min_max_map: ", target_dist_map)
        # for i, row in enumerate(target_dist_map):
        #     print("i: ", i)
        #     print("row: ", row)
        #     print()

        visited = [False] * n
        for i in range(n):
            c = int(s[i])

            # If we don't have c in target, retur False
            if target_dist_map[i][c][0] == -1 and target_dist_map[i][c][1] == -1:
                return False

            # Going left
            if (
                target_dist_map[i][c][0] != -1
                and visited[i - target_dist_map[i][c][0]] is False
            ):
                visited[i - target_dist_map[i][c][0]] = True
                for j in range(0, c):
                    if (
                        target_dist_map[i][j][0] != -1
                        and target_dist_map[i][j][0] < target_dist_map[i][c][0]
                    ):
                        return False

            # Going right
            if (
                target_dist_map[i][c][1] != -1
                and visited[i + target_dist_map[i][c][1]] is False
            ):
                visited[i + target_dist_map[i][c][1]] = True
                for j in range(c + 1, 10):
                    if (
                        target_dist_map[i][j][1] != -1
                        and target_dist_map[i][j][1] < target_dist_map[i][c][1]
                    ):
                        # print("ya")
                        # print("i: ", i)
                        # print("c: ", c)
                        # print("j: ", j)
                        # print("target_dist_map[i][c][1]: ", target_dist_map[i][c][1])
                        # print("target_dist_map[i][j][1]: ", target_dist_map[i][j][1])
                        return False

        return True


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("84532", "34852"),
        ("34521", "23415"),
        # ("12345", "12435"),
        # ("18", "28")
    ]

    for s, t in q:
        print("s: ", s)
        print("t: ", t)
        print()
        answer = solution.isTransformable(s, t)
        print("answer: ", answer)
        print("=====================")
        print()
