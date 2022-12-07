#Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s: str) -> int:
    subset = list()
    maxsubcount = 0
    runningsubcount = 0
    for i in range(len(s)):
        if s[i] not in subset :
            subset.append(s[i])
            runningsubcount = len(subset)
            if runningsubcount > maxsubcount:
                maxsubcount = runningsubcount
        else:
            tempi= subset.index(s[i]) +1
            if len(subset) == tempi:
                subset.clear()
            else:
                subset=subset[tempi:]
            subset.append(s[i])
            runningsubcount = len(subset)
    return ( maxsubcount )

s="abcabcbb"
print(lengthOfLongestSubstring(s))