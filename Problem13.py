'''Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

'''
def longestSubstring(string, k):
    start, end = 0, k
    max_len = k
    while end <= len(string):
        if len(set(string[start:end])) <= k:
            current_len = end - start
            if current_len >= max_len:
                max_len = current_len
            end += 1
        else:
            start += 1
    return max_len

s=input()
k=int(input())
print(longestSubstring(s,k))