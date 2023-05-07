
def evaluatePostfixExpression(expression):
    st = []

    for i in range(len(expression)):
        c = expression[i]

        if (c >= '0' and c <= '9'):
            temp = int(c)
            st.append(temp)
        else:
            op1 = st.pop()
            op2 = st.pop()

            if (c == '+'):
                st.append(op2 + op1)
            elif (c == '-'):
                st.append(op2 - op1)
            elif (c == '*'):
                st.append(op2 * op1)
            elif (c == '/'):
                st.append(op2 / op1)
                
    return st.pop()
expression = "25*46+*"
print(evaluatePostfixExpression(expression))
