class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""

        comp = ''
        count = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1] and count < 9:
                count += 1
            else:
                comp += str(count) + word[i - 1]
                count = 1

        comp += str(count) + word[-1]

        return comp

    

sol = Solution()
print(sol.compressedString("abcde"))
print(sol.compressedString("aaaaaaaaaaaaaabb"))
print(sol.compressedString("aaaaaaaaa"))



# Input: word = "abcde"

# Output: "1a1b1c1d1e"

# Input: word = "aaaaaaaaaaaaaabb"

# Output: "9a5a2b"