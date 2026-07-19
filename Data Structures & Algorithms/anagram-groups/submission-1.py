class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map to compare; have a key
        # loop over and join and sort the letters (which are the index [])
        hashMap = {}

        for s in strs:
            key = "".join(sorted(s))
            
            if key not in hashMap:
                hashMap[key] = []

            hashMap[key].append(s)

        return list(hashMap.values())
