class Solution:

    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []

        while a > 0 or b > 0:
            write_a = False
            l = len(res)

            # Check if we are forced to write 'a' or 'b' to avoid 3 consecutive characters
            if l >= 2 and res[-1] == res[-2]:
                if res[-1] == "b":
                    write_a = True
            else:
                # Otherwise, greedily pick the character with the larger remaining count
                if a >= b:
                    write_a = True

            if write_a:
                res.append("a")
                a -= 1
            else:
                res.append("b")
                b -= 1

        return "".join(res)