class Solution:
    def decodeString(self, s: str) -> str:
        L = len(s)
        stack = []

        def decode(s, idx):
            nonlocal L
            if idx == L:
                return 

            if s[idx] == ']':
                curr = deque()
                while stack[-1] != '[':
                    curr.appendleft(stack.pop())

                
                stack.pop()
                k = deque()
                while stack and stack[-1].isdigit():
                    k.appendleft(stack.pop())

                if not k: 
                    k = 1

                else:   
                    k = int(''.join(k))   

                stack.append(k * ''.join(list(curr)))

                decode(s, idx + 1)
            else:
                stack.append(s[idx])
                decode(s, idx + 1)


                    


        decode(s, 0)
        return ''.join(stack)

        