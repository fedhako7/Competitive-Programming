class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        while len(bits) > 2:
            if bits[0] == 1:
                bits = bits[2:]
            else:
                bits = bits[1:]

        if bits in [[0], [0,0]]: return True
        return False

        
        