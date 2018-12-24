#python version 3.5, all 3.x is ok
import sys
sys.path.append('../../')
sys.path.append('.')
from work3.work_info.utils import * # (./utils)make pycharm happy

def train(trainData,trainLabel):
    #w 数据维数行，1列
    w = np.array([0,0],float).transpose()
    b = 0
    lrate = 1
    # --------------------------------------------
    # algorithm start here
    a = np.zeros(trainData.shape[1])
    cnt = 1
    # generate Gram matrix
    G = np.zeros([trainData.shape[1], trainData.shape[1]])
    for i in (0, 1, 2):
        for j in (0, 1, 2):
            G[i][j] = np.dot(trainData[:, i], trainData[:, j])
    # while xxxxx
    while cnt:
        cnt = 0
        for i in range(trainData.shape[1]):
            temp = 0
            for j in range(trainData.shape[1]):
                temp += a[j]*G[i,j]*trainLabel[j]
            if (temp+b)*trainLabel[i] <= 0:
                a[i] += lrate
                b += trainLabel[i] * lrate
                cnt = 1
    for i in range(trainData.shape[1]):
        w += a[i]*trainData[:,i]*trainLabel[i]
    return w, b


if __name__ == "__main__":
    # trainData, trainLabel = generate_dataset_norm(np.array([[0,0],[1,-1]]),[0.1],50)
    # train data: 数据维度行，样本个数列
    trainData, trainLabel = generate_dataset_static()
    w,b = train(trainData, trainLabel)
    plot_data(w,b,trainData,trainLabel)
