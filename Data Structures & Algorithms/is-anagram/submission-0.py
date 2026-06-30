class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        for ch in t:
            count[ch]=count.get(ch,0)-1
        if all(value==0 for value in count.values()):
            return True
        else:
            return False