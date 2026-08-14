class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        visited = {}

        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in visited:
                visited[s[right]]+=1
            else:
                visited[s[right]] = 1

            while visited[s[right]] > 2:
                visited[s[left]]-=1
                left+=1

            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
        
        return max_len