class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)


        if len(palindrome) == 1:
            return ''


        for idx in range(len(palindrome) // 2):
            if palindrome[idx] != 'a':
                palindrome[idx] = 'a'
                return ''.join(palindrome)

        palindrome[-1] = 'b'
        return ''.join(palindrome)


