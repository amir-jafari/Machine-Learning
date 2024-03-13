import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ----------------------------------------------------------------------------------------------------
def lr_reduce(epoch):
    lr_decay = 0.8
    lr_max = 0.005
    lr_min = 0.001
    lr = (lr_max - lr_min) * lr_decay ** epoch + lr_min
    return lr


# ----------------------------------------------------------------------------------------------------
plt.figure()
plt.plot(np.arange(20), [lr_reduce(ep) for ep in range(20)])
plt.show()


# ----------------------------------------------------------------------------------------------------
def lr_increase_decrease(epoch):
    lr_0 = 0.001
    lr_0_steps = 5
    lr_max = 0.005
    lr_max_steps = 5
    lr_min = 0.0005
    lr_decay = 0.8

    if epoch < lr_0_steps:
        lr = ' '  # TODO
    elif epoch < lr_0_steps + lr_max_steps:
        lr = ' '  # TODO
    else:
        lr = ' '  # TODO

    return lr


# ----------------------------------------------------------------------------------------------------
plt.figure()
plt.plot(np.arange(30), [lr_increase_decrease(ep) for ep in range(30)])
plt.show()


# ----------------------------------------------------------------------------------------------------
class lr_inc_dec:
    def __init__(self, lr_0=0.001, lr_0_steps=5, lr_max=0.005, lr_max_steps=5, lr_min=0.0005, lr_decay=0.9):
        self.lr_0 = lr_0
        self.lr_max = lr_max
        self.lr_0_steps = lr_0_steps
        self.lr_max_steps = lr_max_steps
        self.lr_min = lr_min
        self.lr_decay = lr_decay

    def __call__(self, epoch):
        # TODO

        return self.lr


# ----------------------------------------------------------------------------------------------------
lr_scheduler = lr_inc_dec(lr_0=0.002, lr_0_steps=10, lr_max=0.01, lr_max_steps=5, lr_min=0.001, lr_decay=0.85)

plt.figure()
plt.plot(np.arange(50), [lr_scheduler(ep) for ep in range(50)])
plt.show()
# ----------------------------------------------------------------------------------------------------

P = ' '  # TODO
T = ' '  # TODO
print(P)
print(T)


# ----------------------------------------------------------------------------------------------------

class simplenet:
    def __init__(self, weight, bias):
        self.w = weight
        self.b = bias

    def sim(self, p):
        return  # TODO

    def deriv(self, p):
        return  # TODO


# ----------------------------------------------------------------------------------------------------

net = simplenet(1, 0)
A = net.sim(P)
print(A)
dA_dwb = net.deriv(P)
print(dA_dwb)


# ----------------------------------------------------------------------------------------------------

class mse:
    def value(self, a, t):
        perf = ' '  # TODO
        return perf

    def deriv(self, a, t):
        df_da = ' '  # TODO
        return df_da


# ----------------------------------------------------------------------------------------------------

test_mse = mse()
performance = test_mse.value(A, T)
print(performance)
dF_dA = test_mse.deriv(A, T)
print(dF_dA)


# ----------------------------------------------------------------------------------------------------


def train_gd(net, perf, lr_sched, max_epoch, data):
    pp = data['Input']
    tt = data['Target']
    ff = []
    for ep in range(max_epoch):
        ' '  # TODO
    return net, ff


# ----------------------------------------------------------------------------------------------------

lr_scheduler = lr_inc_dec(lr_0=0.01, lr_0_steps=10, lr_max=0.03, lr_max_steps=5, lr_min=0.02, lr_decay=0.85)
DATA = {'Input': P, 'Target': T}
PERF = mse()
MAX_EPOCH = 30
NET = simplenet(0.1, 0.1)

# ----------------------------------------------------------------------------------------------------
NET2, FF = train_gd(NET, PERF, lr_scheduler, MAX_EPOCH, DATA)
# ----------------------------------------------------------------------------------------------------
plt.figure()
plt.plot(np.arange(MAX_EPOCH), FF)
plt.show()

# ----------------------------------------------------------------------------------------------------
sample_df = pd.read_csv(
    'https://raw.githubusercontent.com/NNDesignDeepLearning/NNDesignDeepLearning/master/05.PythonChapter/Code/ChapterNotebook/SampleDF.csv?token=AUZTTDQALCLLAYUY2ZZGDKDA5YTEK')
# ----------------------------------------------------------------------------------------------------
print(sample_df.head())

mean_fvc = ' '  # TODO
std_fvc = ' '  # TODO
mean_percent = ' '  # TODO
std_percent = ' '  # TODO
# ----------------------------------------------------------------------------------------------------
sample_df['FVC'] = ' '  # TODO
sample_df['Percent'] = ' '  # TODO

# ----------------------------------------------------------------------------------------------------
P = ' '  # TODO
T = ' '  # TODO

# ----------------------------------------------------------------------------------------------------
Data = {'Input': P, 'Target': T}


# ----------------------------------------------------------------------------------------------------


def data_gen(data, bsize):
    In = data['Input']
    Tar = data['Target']
    num = len(In)
    steps = num // bsize
    epoch = 0
    while True:
        for ii in range(steps):
            yield epoch,  # TODO
        # TODO
        epoch += 1


# ----------------------------------------------------------------------------------------------------

def train_gd_gen(net, perf, lr_sched, max_epoch, datagen):
    ff = []
    ep = 0
    while ep < max_epoch:
        ' '  # TODO
    return net, ff


# ----------------------------------------------------------------------------------------------------
lr_scheduler = lr_inc_dec(lr_0=0.001, lr_0_steps=10, lr_max=0.01, lr_max_steps=10, lr_min=0.000001, lr_decay=0.85)
DATA = {'Input': P, 'Target': T}
BSIZE = 10
PERF = mse()
MAX_EPOCH = 50
NET = simplenet(0.1, 0.1)
gendata = data_gen(DATA, BSIZE)

# ----------------------------------------------------------------------------------------------------

NET2, FF = train_gd_gen(NET, PERF, lr_scheduler, MAX_EPOCH, gendata)
# ----------------------------------------------------------------------------------------------------
plt.figure()
plt.plot(FF)
plt.show()
# ----------------------------------------------------------------------------------------------------

pp = np.arange(-3, 3, 0.1)
aa = NET2.sim(pp)
plt.plot(pp, aa, 'r', P, T, 'b.')

# ----------------------------------------------------------------------------------------------------
