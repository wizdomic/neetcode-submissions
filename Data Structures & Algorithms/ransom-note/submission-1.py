class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_map = Counter(ransomNote)
        magazine_map = Counter(magazine)
        
        for char, ransomNote_count in ransomNote_map.items():
            if not magazine_map.get(char) or magazine_map.get(char) < ransomNote_count:
                return False
        return True