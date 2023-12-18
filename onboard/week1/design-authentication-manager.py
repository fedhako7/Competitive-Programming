class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.life_time = timeToLive
        self.expire_time = 0
        self.token_id = None
        self.tokens = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expire_time = self.life_time + currentTime
        self.token_id = tokenId
        self.tokens[self.token_id] = self.expire_time

        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if self.tokens[tokenId] > currentTime:
                self.tokens[tokenId] = self.life_time + currentTime


    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.tokens:
            if self.tokens[token] > currentTime:
                count += 1

        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)