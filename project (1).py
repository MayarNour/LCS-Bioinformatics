import cv2
from past.builtins import xrange

image = cv2.imread("unnamed.jpg")

def lcs(X, Y, m, n):
    L = [[0 for x in xrange(n + 1)] for x in xrange(m + 1)]
    a=20
    b=30

    for i in xrange(m + 1):
        a = a + 40
        b = 30
        for j in xrange(n + 1):
            if i == 0:
                L[i][j] = 0
                cv2.putText(image, str(L[i][j]), (a , b), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (80, 170, 89), 1, 1)
            elif j==0:
                L[i][j] = 0
                cv2.putText(image, str(L[i][j]), (a, b), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (80, 170, 89), 1, 1)
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                cv2.putText(image, str(L[i][j]), (a, b), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (80, 170, 89), 1, 1)
                cv2.arrowedLine(image, (a-5,b-5), (a-30,b-20),(0,0, 255) , 1)
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                cv2.putText(image, str(L[i][j]), (a, b), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (80, 170, 89), 1, 1)
                if(L[i - 1][j]>L[i][j - 1]):
                    cv2.arrowedLine(image, (a - 5, b - 5), (a - 30, b - 5), (0, 0, 255), 1)
                elif(L[i - 1][j] <L[i][j - 1]):
                    cv2.arrowedLine(image, (a - 5, b - 5), (a - 5, b - 20), (0, 0, 255), 1)
                else:
                    cv2.arrowedLine(image, (a - 7, b - 5), (a - 30, b - 5), (0, 0, 255), 1)
                    cv2.arrowedLine(image, (a - 5, b - 7), (a - 5, b - 20), (0, 0, 255), 1)
            b = b + 20

    index = L[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""
    i = m
    j = n
    b=b-20
    cv2.putText(image, str(L[i][j]), (a, b), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 70, 89), 1, 1)
    while i >0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            a=a-40
            b=b-20
            cv2.putText(image, str(L[i][j]), (a, b), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 70, 89), 1, 1)
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
            a=a-40
            cv2.putText(image, str(L[i][j]), (a, b), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 70, 89), 1, 1)
        else:
            b = b - 20
            j -= 1
            cv2.putText(image, str(L[i][j]), (a, b), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 70, 89), 1, 1)
    cv2.putText(image,"".join(lcs), (9, 21), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (25, 70, 189), 1, 1)
    print("LCS of " + X + " and " + Y + " is " + "".join(lcs))

X = "ABCDA"
Y = "ACBDEA"
m = len(X)
n = len(Y)
cv2.putText(image, "LCS is:", (5, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (25, 70, 189), 1, 1)
v=15 #fpr b
c=100
for i in range(m):
    cv2.putText(image, str(X[i]), (c, v), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (25, 70, 189), 1, 1)
    c=c+40
c=40
v=50
for i in range(n):
    cv2.putText(image, str(Y[i]), (c, v), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (25, 70, 189), 1, 1)
    v= v + 20

lcs(X, Y, m, n)
cv2.imwrite("eng.png",image)
cv2.imshow("Longest common subsequence",image)
cv2.waitKey()