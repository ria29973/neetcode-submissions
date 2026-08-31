class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            for c in string:
                encode += str(ord(c))
                encode += " "
            encode += "*"
        return encode
        # "abc ab" --> "1 2 3*1 2"
        

    def decode(self, s: str) -> List[str]:
        #"1 2 3*1 2"
        #number = "1"
        decode = []
        word = ""
        number = ""
        for c in s:
            if c == "*":
                decode.append(word)
                word = ""
                number = ""
            elif c == " ":
                char = chr(int(number))
                word+=char
                number = ""
            else:
                number += c
        return decode
                
            

