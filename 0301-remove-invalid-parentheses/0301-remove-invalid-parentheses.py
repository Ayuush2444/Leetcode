class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_rem = 0
        right_rem = 0

        for ch in s:
            if ch == '(':
                left_rem += 1

            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        result = set()

        def backtrack(index, path, balance, left_rem, right_rem):

            if index == len(s):
                if balance == 0 and left_rem == 0 and right_rem == 0:
                    result.add(''.join(path))
                return

            ch = s[index]

            if ch == '(' and left_rem > 0:
                backtrack(
                    index + 1,
                    path,
                    balance,
                    left_rem - 1,
                    right_rem
                )

            elif ch == ')' and right_rem > 0:
                backtrack(
                    index + 1,
                    path,
                    balance,
                    left_rem,
                    right_rem - 1
                )
            if ch != '(' and ch != ')':
                path.append(ch)

                backtrack(
                    index + 1,
                    path,
                    balance,
                    left_rem,
                    right_rem
                )

                path.pop()

            elif ch == '(':
                path.append(ch)

                backtrack(
                    index + 1,
                    path,
                    balance + 1,
                    left_rem,
                    right_rem
                )

                path.pop()

            else:  
                if balance > 0:
                    path.append(ch)

                    backtrack(
                        index + 1,
                        path,
                        balance - 1,
                        left_rem,
                        right_rem
                    )

                    path.pop()

        backtrack(0, [], 0, left_rem, right_rem)

        return list(result)