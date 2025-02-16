"""
NOTE: My initial solution was getting time limit exceeded and I was left wondering why the fuck I was so bad at python.
Here are the reasons:
1) I was checking if I arrived at the correct state after popping the element from queue.
This was a mistake since you can just check if you have arrived BEFORE (or after really) putting the element into the queue.
When you are ready to put an element into the queue, you can check if that element is the answer.
But this fix was not enough to get the solution accepted.

2) I was using arrays instead of deque for queues.
But this fix as well was not enough for the solution to get accepted so I peeked into Solutions tab in leetcode.

3) I had to turn deadends from a list to a set!!!
This way the lookup time was reduced to O(1) which yielded amazing results.
Such a simple fix but changes the runtime completely.
Thanks to the GOAT Mohammed Raziullah Ansari for this fix!!!
(https://leetcode.com/problems/open-the-lock/solutions/5057116/faster-lesser-detailed-explaination-bfs-step-by-step-explaination-python-java-c/)
"""


from collections import deque


class Solution:
    def openLock(self, deadends, target):
        # So fucking interesting, without this the code is SLOW AS SHIT
        # But turning the deadends into a set lowers the lookup time from O(n) to O(1). AMAZING!
        deadends = set(deadends)

        # Edge cases
        if "0000" in deadends or target in deadends:
            return -1
        if target == "0000":
            return 0

        queue = deque([('0000', 0)])
        visited = {'0000'}
        answer = -1

        while queue:
            (state, ans) = queue.popleft()

            if answer != -1:
                break

            arr = [int(c) for c in state]

            d = [-1, 1]

            def get_state(arr):
                state = ''
                for num in arr:
                    if num < 0:
                        state += '9'
                    elif num > 9:
                        state += '0'
                    else:
                        state += str(num)
                return state

            for i in d:
                for j in [0, 1, 2, 3]:
                    arr_c = list(arr)
                    arr_c[j] += i
                    new_state = get_state(arr_c)
                    if new_state not in deadends and new_state not in visited:
                        if new_state == target:
                            answer = ans + 1

                        queue.append((new_state, ans + 1))
                        visited.add(new_state)

        return answer


if __name__ == "__main__":
    solution = Solution()

    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"

    print('deadends: ', deadends)
    print('target: ', target)
    print('\n')
    answer = solution.openLock(deadends, target)
    print('answer: ', answer)
