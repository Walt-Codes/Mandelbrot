import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

from MandelbrotSet import MandelbrotSet

if __name__ == '__main__':
    mset = MandelbrotSet()
    res = mset.res
    target = [-0.1529, 1.0397]
    numFrames = 100
    fig, ax = plt.subplots()
    x = np.empty(res*res)
    y = np.empty(res*res)
    colors = np.empty(res*res)
    rate = np.log(0.1)/np.log(mset.scale)

    def update(f):
        plt.clf()

        for i in range(res):
            for j in range(res):
                xval = target[0] + (mset.scale ** f)*(2 * (j+1 - res / 2) / res)
                yval = target[1] + (mset.scale ** f)*(2 * (i+1 - res / 2) / res)
                index = i * res + j
                x[index] = xval
                y[index] = yval
                colors[index] = mset.calc_value(xval, yval, 3*f, int(np.floor(f/rate+4)))
        print("hits: "+str(mset.hits))
        print("misses: " + str(mset.misses))
        mset.hits = 0
        mset.misses = 0
        maxcol = max(colors)
        for c in range(res*res):
            colors[c] = colors[c]/maxcol

        plt.scatter(x, y, c=colors, s=50, cmap="BuPu")

    ani = animation.FuncAnimation(fig, update, interval=100, frames=numFrames)
    writervideo = animation.PillowWriter(fps=20)
    ani.save(mset.fullFilename()+"_"+str(target)+".gif", writer=writervideo)
    plt.close()
    # plt.show()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
