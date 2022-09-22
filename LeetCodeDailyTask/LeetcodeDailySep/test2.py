# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
class Solution:
    def reverseWords(self, s: str) -> str:
        r_word = [word[::-1] for word in s.split()]
        return " ".join(r_word)


x = Solution()
print(x.reverseWords("Let's take LeetCode contest"))