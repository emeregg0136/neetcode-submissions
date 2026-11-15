class Solution:

    def encode(self, strs: List[str]) -> str:
        
        def get_three_digits(self, length: int) -> str:
            if length < 10:
                length = "00" + str(length)
            elif length < 100:
                length = "0" + str(length)
            elif length < 1000:
                length = str(length)
            return length
        
        encoded = ""

        size_list = get_three_digits(self, len(strs))
        encoded += size_list
        
        for word in strs:
            l = len(word)
            length = get_three_digits(self, l)

            encoded += length 
            encoded += word

        print(encoded)
        return encoded


    def decode(self, st: str) -> List[str]:

        decoded = []

        def get_length(self, st):
            length = st[:3]
            
            i = 0 
            while length[i] == 0:
                i += 1

            length = int(st[i:3])
            remains = st[3:]
            return length, remains
        
        def get_word(self, length, st):
            word = st[:length]
            remains = st[length:]
            return word, remains
            
        num_words, remains = get_length(self, st)
        
        for i in range(num_words):
            length, remains = get_length(self, remains)
            word, remains = get_word(self, length, remains)
            decoded.append(word)
        
        return decoded


            
        
