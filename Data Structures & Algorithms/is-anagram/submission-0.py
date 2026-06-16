class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        user_input = ""
        return sorted(s.lower()) == sorted(t.lower())

        print(f'{user_input}')