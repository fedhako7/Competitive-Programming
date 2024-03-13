class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        

        grammar = [0]
        def constructGrammar():
            nonlocal n, k, grammar
            if n == 1:
                return

            curr = []
            for dig in grammar:
                if dig == 0:
                    curr.append(0)
                    curr.append(1)
                else:
                    curr.append(1)
                    curr.append(0)

                grammar = curr[:]

            middle = len(grammar) // 2
            if k > (2 ** (n - 2)):
                k -= (2 ** (n - 2))
                grammar = grammar[middle: ]
            else:
                grammar = grammar[ :middle]

            n -= 1
            constructGrammar()

        constructGrammar()
        return grammar[k - 1]


            
