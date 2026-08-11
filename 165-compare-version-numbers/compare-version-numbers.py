class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        num1 = version1.split('.')
        num2 = version2.split('.')

        max_len = max(len(num1) , len(num2))

        for i in range(max_len):
            v1 = int(num1[i]) if i < len(num1) else 0
            v2 = int(num2[i]) if i < len(num2) else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            
        return 0 