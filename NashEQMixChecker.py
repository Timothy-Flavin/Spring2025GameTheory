import numpy as np
import matplotlib.pyplot as plt


def util(pY,pA):
    u1 = pY*(0.3*pA + 0.2*(1-pA)) + (1-pY)*(0.2*pA + 0.4*(1-pA))
    u2 = pY*(4*pA + 3*(1-pA)) + (1-pY)*(0*pA + 2*(1-pA))


    #print(f"u1 {u1}, {3*pY*pA-2*pY-2*pA+4}")
    #print(f"u2 {u2}, {3*pY*pA+pY-2*pA+2}")
    #input()
    return u1,u2

def graph():
    pY = np.arange(0,100,1,dtype=np.int32)
    pA = np.arange(0,100,1,dtype=np.int32)

    u1 = np.zeros((100,100))
    u2 = np.zeros((100,100))

    for i in range(100):
        for j in range(100):
            u1[i,j],u2[i,j] = util(pY[i]/100,pA[j]/100)

    plt.imshow(u1,origin='lower',cmap='viridis')
    plt.title('Utility of player 1')
    plt.legend()
    plt.show()

    plt.imshow(u2,origin='lower',cmap='viridis')
    plt.title('Utility of player 2')
    plt.legend()
    plt.show()


def NE(pA):
    pY,pA=2/3,2/3 
    slr = 0.001
    step=100
    while True:
        lr = slr*(100/step)
        u1,u2 = util(pY,pA)
        c = True

        if pA <= 1-lr and u2 < util(pY,pA+lr)[1]:
            pA += lr
            c=False
        elif pA >= lr and u2 < util(pY,pA-lr)[1]:
            pA -= lr
            c=False

        if pY <= 1-lr and u1 < util(pY+lr,pA)[0]:
            pY += lr
            c=False

        elif pY >= lr and u1 < util(pY-lr,pA)[0]:
            pY -= lr
            c=False
        
        print(f"py {pY},pa {pA}, util1 {u1}, util2 {u2}, lr {lr}")
        step+=1
        if c:
            break

if __name__ == '__main__':
    graph()
    NE(0.5)