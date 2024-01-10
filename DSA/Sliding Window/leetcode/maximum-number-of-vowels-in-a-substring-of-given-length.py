class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        curr_vowel = 0
        max_vowel = 0
    
        for char in s[ :k]:
            if char in vowels:
                curr_vowel += 1
                max_vowel += 1

        for idx in range(k, len(s)):
            if s[idx] in vowels:
                curr_vowel += 1
                
            if s[idx - k] in vowels:
                curr_vowel -= 1

            max_vowel = max(max_vowel, curr_vowel)

        return max_vowel
