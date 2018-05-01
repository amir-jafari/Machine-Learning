# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Pandas Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
import pandas as pd
import numpy as np
# ----------------------------------------------------------------------------------
# ---------------------- Panda Series------------------------------------------------
p1 = pd.Series([1, 2, 3, 4])

type(p1)
p2 = p1.values
print(p2)

# ----------------------------------------------------------------------------------
# ---------------------- TimeStamps  ------------------------------------------------

pd.date_range(start='20170101', end='20170331', freq='D')
pd.date_range(start='20170101', end='20170331', freq='M')
pd.date_range(start='20170101', freq='M', periods=4)

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Method----------------------------------------------
norm_series = pd.Series(np.floor(np.random.normal(50, 12, 100)))
print(norm_series)

norm_series = pd.Series(np.random.normal(50, 12, 100))
print(norm_series)


p2 = norm_series.shape
print(p2)
p3 = norm_series.mean()
print(p3)
p4 = norm_series.median()
print(p4)
p5 = norm_series.std()
print(p5)
p6 = norm_series.unique()
print(p6)
p7 = norm_series.nunique()
print(p7)
p8 = norm_series.argmin()
print(p8)
p9 = norm_series.argmax()
print(p9)
p10 = norm_series.rank()
print(p10)
p11 = norm_series.rank(ascending=False)
print(p11)
p12 = norm_series.sort_values()
print(p12)
p13 = norm_series.cumsum()
print(p13)
p14 = norm_series.view()
print(p14)
# ----------------------------------------------------------------------------------
# ---------------------- Pandas DataFrame-------------------------------------------

times = pd.timedelta_range('14:37:55', freq='10S', periods=13)
heights = pd.Series([7, 938, 4160, 9872, 17635, 26969, 37746, 50548, 66033, 83966, 103911, 125512, 147411])

sts121 = pd.DataFrame({'Timestamp': times, 'Altitude': heights})
print(sts121)
type(sts121)

shape_ = sts121.shape
print(shape_)

p15 = sts121.columns
print(p15)

p16 = sts121.info()
print(p16)

p17 = sts121.describe()
print(p17)

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Extract Data----------------------------------------

p18 = sts121['Altitude']
print(p18)


select_cols = ['Timestamp', 'Altitude']
p19 = sts121[select_cols]
print(p19)


final_height = sts121.iloc[12, :]
final_height = sts121.iloc[12]
final_height1 = sts121.iloc[12,]

p20 = final_height == final_height1
print(p20)
# ----------------------------------------------------------------------------------
# ---------------------- Pandas Setindex--------------------------------------------

sts121_1 = sts121.set_index('Timestamp')
print(sts121_1)

index = sts121_1.index
print(index)

original = sts121.set_index('Timestamp', inplace=True)
print(original)



# ----------------------------------------------------------------------------------
# ---------------------- Pandas loc and iloc----------------------------------------
find_loc = sts121.loc['14:38:55']
print(find_loc)

p21 = sts121.iloc[6]
print(p21)

sts121 = sts121.reset_index()
print(sts121.index)
