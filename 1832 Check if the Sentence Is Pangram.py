class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        memo = set()
        
        for char in sentence:
            memo.add(char)
        
        return len(memo)==26