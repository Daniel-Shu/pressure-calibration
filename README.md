# pressure-calibration
calibrate the pressure sensor with the 压力计
##V1.0
** calibrate-oressure.py**使用串口读取HANDPI压力数据，并通过串口读取拐杖板数据，将读取到的数据显示并保存；
** readCsv2Fit.py**读取csv文件中的压力值和ADC值，并使用matplpotlib、numpy来最后拟合成一条直线，输出得到直线的参数