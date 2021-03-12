# Sliding Window
# March 3, 2021

def lengthOfLongestSubstring(self, s: str) -> int:
    max_count = 0
    start = 0
    chars = {}
    
    for end in range(len(s)):
        if s[end] not in chars:
            chars[s[end]] = 1
        else:
            chars[s[end]] += 1
            while chars[s[end]] > 1:
                letter = s[start]
                if letter in chars:
                    if chars[letter] > 1:
                        chars[letter] -= 1
                    else:
                        del chars[letter]
                start += 1
        
        max_count = max(max_count, end-start+1)
    return max_count