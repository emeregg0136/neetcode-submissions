class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_dict = {}

        for word in strs:
            key = [0]*26
            for letter in word:
                index = ord(letter) - ord('a')
                key[index] += 1

            if key_dict.get(str(key)) == None:
                key_dict[str(key)] = [word]
            else:
                key_dict[str(key)].append(word)

        return list(key_dict.values())
