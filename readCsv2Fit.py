# coding:utf-8

import csv
# import numpy.polynomial.polynomial as poly
import numpy
import matplotlib.pyplot as plt
reader = csv.reader(open("ceshi__1463635386.11.csv", 'rb'))
adc = []
pre = []
for item in reader:
    # print item
    pre.append(int(item[0]))
    adc.append(float(item[1]))

print len(adc)

# coefs = poly.polyfit(adc, pre, 1)
# ffit = poly.polyval(x_new, coefs)
# plt.plot(x_new, ffit)
# print len(coefs)
gain = numpy.polyfit(adc, pre, 1)
# print ("%.8f %.8f" % (numpy.polyfit(adc, pre, 1)))
print ("%.10f %.10f" % (gain[0], gain[1]))

# minX = numpy.array(adc).argmin()
# maxX = numpy.array(adc).argmax()
minX = min(enumerate(adc), key=lambda x: x[1])[-1]
maxX = int(max(enumerate(adc), key=lambda x: x[1])[-1])

print minX
print maxX
x = numpy.linspace(minX, maxX, num=5000)

# y = numpy.polyval(x, gain)

y = gain[0] * x + gain[1]
# y = []
# for i in xrange(0, len(x)):
#     pass
#     y.append(gain[0] * x[i] + gain[1])
# print len(x)
# print y
plt.figure(1)  # 创建图表1
# plt.plot(adc, pre)
plt.plot(x, y, color='red')
plt.plot(adc, pre)
plt.show()
