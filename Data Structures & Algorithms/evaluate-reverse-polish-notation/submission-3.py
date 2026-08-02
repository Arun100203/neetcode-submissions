class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i == '+':
                temp1 = st.pop()
                temp2 = st.pop()
                st.append(temp2 + temp1)
            elif i == '-':
                temp1 = st.pop()
                temp2 = st.pop()
                st.append(temp2 - temp1)
            elif i == '*':
                temp1 = st.pop()
                temp2 = st.pop()
                st.append(temp2 * temp1)
            elif i == '/':
                temp1 = st.pop()
                temp2 = st.pop()
                st.append(int(temp2 / temp1))
            else:
                st.append(int(i))

        return (st.pop())
        