class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,num:int):
        node = self.root

        for i in range(31,-1,-1):
            bit = (num>>i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            
    def getMax_Xor(self,num:int)-> int:
        node = self.root
        max_xor = 0
        for i in range(31,-1,-1):
            bit = (num>>i) & 1
            opposite_bit = 1 - bit

            if opposite_bit in node.children:
                max_xor |= (1<<i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
            
        return max_xor

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        nums.sort()

        offline_queries = []

        for i , (x,m) in enumerate(queries):
            offline_queries.append((m,x,i))
        
        offline_queries.sort()
        
        ans = [-1] * len(queries)
        trie = Trie()
        nums_idx = 0
        n = len(nums)

        for m , x , original_idx in offline_queries:
            while nums_idx < n and nums[nums_idx] <= m:
                trie.insert(nums[nums_idx])
                nums_idx+=1
            
            if nums_idx == 0:
                continue

            ans[original_idx] = trie.getMax_Xor(x)

        return ans
