import numpy as np
import matplotlib.pyplot as plt

def F(x):
    """
    input:  x  
    output: trả về giá trị của hàm F(x)
    """
    return x * x - 5 * np.sin(x)

def f(x):
    """
    input: x
    output: trả về giá trị của đạo hàm F(x)
    """
    return 2 * x - 5 * np.cos(x)

def findX(LR,xold,loop):
    """
    input: 
         LR: learningRate (Hằng số học)
         xold: Điểm x ban đầu
         loop: số vòng lặp
    output:
        trả về giá trị cực tiểu của hàm số
    """
    xnew = xold
    for i in range(loop):
        xnew = xnew - LR * f(xnew)
        if f(xnew) <= 1e-6:
            break
    return xnew
    


X = findX(0.001,4,1000)
print("x = :",X)



"""
vẽ hình
"""
A = np.linspace(-5, 4,100)
plt.plot(A,F(A))
plt.title("$F(x) = x^2 - 5 \cdot sin(x)$")
plt.scatter(X,F(X),color='red')
plt.annotate("Global_Minimun", xy = (X,F(X)) , xytext = (0,3),arrowprops=dict(facecolor='red', shrink=1))
plt.show()
plt.savefig("output.png")

