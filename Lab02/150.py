class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                st.append(int(t))
            else:
                b, a = st.pop(), st.pop()
                if t == "+": st.append(a + b)
                elif t == "-": st.append(a - b)
                elif t == "*": st.append(a * b)
                else: st.append(int(a / b))
        return st[0]