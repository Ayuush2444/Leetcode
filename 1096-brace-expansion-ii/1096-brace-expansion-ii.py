class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def parse(i):
            result = set()
            if expression[i] == '{':
                i += 1

                while True:
                    part, i = parse(i)
                    result |= part

                    if expression[i] == ',':
                        i += 1
                    else:
                        break

                i += 1 

            else:
                result.add(expression[i])
                i += 1
            while i < n and expression[i] not in '},':
                part, i = parse(i)

                new_result = set()

                for a in result:
                    for b in part:
                        new_result.add(a + b)

                result = new_result

            return result, i

        result, _ = parse(0)

        return sorted(result)