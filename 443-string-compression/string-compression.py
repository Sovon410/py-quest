class Solution:
    def compress(self, chars: List[str]) -> int:
        lnt = len(chars)
        idx = 0
        i = 0

        while i < lnt:
            ch = chars[i]
            count = 0

            while i < lnt and chars[i] == ch:
                count += 1
                i += 1

            chars[idx] = ch
            idx += 1

            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1

        return idx