# -*- coding:utf-8 -*-
#例6.17二维数组的基本要点
import numpy as np

#python的list比较难符合书上的例子,所以用python的库numpy来做例子

array_a = np.ndarray(shape=(10,20))
array_b = np.ndarray(shape=(20))
first_place = 5
array_a[first_place][10] = 6
array_b[7] = array_a[5,10]
print array_a[5][2*first_place]
print array_b[7]