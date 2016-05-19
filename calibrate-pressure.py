# coding:utf-8

import serial
import sys
# import glob
from time import *
import string
import getopt

""" Lists serial port names

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of the serial ports available on the system
"""

"""
print "Checking for the Serial Port..."

# just config the serial port according to the platform we use
if sys.platform.startswith('win'):
    ports = ['COM%s' % (i + 1) for i in range(256)]
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    # this excludes your current terminal "/dev/tty"
    ports = glob.glob('/dev/tty[A-Za-z]*')
elif sys.platform.startswith('darwin'):
    ports = glob.glob('/dev/tty.*')
else:
    raise EnvironmentError('Unsupported platform')

# print ports


"""
# for port in ports:
#     try:
# print port
#         ser = serial.Serial(port)
#         print ser.portstr
# except Exception, e:
# raise e
#     except (OSError, serial.SerialException):
#         pass
#     finally:
#         ser.close


'''
# input data by our hands

# open serial to get and print the data
try:
    ser = serial.Serial(port='COM11', baudrate=921600, timeout=1)
except Exception, e:
    raise e

filename = "Left" + str(time()) + ".csv"
# filename = "Serial111" + ".csv"
print filename
f = open(filename, 'w')  # (1)

# ser = serial.Serial(port='COM11', baudrate=921600, timeout=1)
while True:
    # try:
    #     ser = serial.Serial(port='COM11', baudrate=921600, timeout=1)
    # except Exception, e:
    #     raise e
    sumSer = 0
    strIput = raw_input("Input the N:")
    if strIput.isdigit():
        i = 0
        for x in xrange(1, 151):
            try:
                ser.flushInput()
                ser.flushOutput()
                dataLine = ser.readline()
                if int(dataLine) < 99999999 and int(dataLine) > 0:
                    pass
                    sumSer = sumSer + int(dataLine)
                    i = i + 1
                # print dataLine,
                # print int(dataLine)

            except Exception, e:
                print e
        print "N: " + strIput,
        print " ---- ADC:" + str(sumSer / i)
        f.write(strIput + ',' + str(sumSer / i) + "\n")
    # ser.close()
f.close()
'''


def hex_show(argv):
    result = ''
    hLen = len(argv)
    for i in xrange(hLen):
        hvol = ord(argv[i])
        hhex = '%02x' % hvol
        result += hhex + ' '
    print 'hexShow:', result
    return result


def hex_resolve(argv):
    serial_head = "55 01 2b 30 30 "
    result = ''
    hLen = len(argv)
    for i in xrange(hLen):
        hvol = ord(argv[i])
        hhex = '%02x' % hvol
        result += hhex + ' '
    # print 'hexShow:', result, serial_head
    # print result.index(serial_head)
    # print False == cmp(serial_head[0:len(serial_head)],
    # result[0:len(serial_head)])

    # if False == cmp(serial_head[0:len(serial_head)], result[0:len(serial_head)]):
    #     pass
    #     print result[16], result[19], result[22]

    # location is the place where can find the serial_head in the result
    location = string.find(result, serial_head)
    len_serial_head = len(serial_head)
    press = 0
    # print location
    if location >= 0:
        pass
        # we need the data after the serial head data <>
        # ex. 55 01 2B 30 30 32 35 32 ==> we need 2 5 2 in the 32 35 32
        # print result[location + len_serial_head + 1], result[location + len_serial_head + 4], result[location + len_serial_head + 7]
        # print int(result[location + len_serial_head + 1], 16), int(result[location + len_serial_head + 4], 16), int(result[location + len_serial_head + 7], 16)
        # print int(result[location + len_serial_head + 1], 16) * (16**2) +
        # int(result[location + len_serial_head + 4], 16) * 16 +
        # int(result[location + len_serial_head + 7], 16)
        press = int(result[location + len_serial_head + 1], 16) * (16 ** 2) + int(result[
            location + len_serial_head + 4], 16) * 16 + int(result[location + len_serial_head + 7], 16)
    else:
        press = 0
    # if (string.find(result, serial_head)):
    #     pass
    # print 'pressure = ', press
    return press


def adc_data_from_ser(serial, num=5, datatype='int'):
    pass
    sumSer = 0.0
    i = 0
    num = num + 1
    for x in xrange(1, num):
        try:
            serial.flushInput()
            serial.flushOutput()
            dataLine = serial.readline()
            if datatype == 'int':
                pass
                if int(dataLine) < 99999999 and int(dataLine) > 0:
                    pass
                    sumSer = sumSer + int(dataLine)
                    i = i + 1
                # print dataLine,
                # print int(dataLine)
            if datatype == 'float':
                pass
                if float(dataLine) < 99999999 and float(dataLine) > 0:
                    pass
                    sumSer = sumSer + float(dataLine)
                    i = i + 1
                # print dataLine,
                # print int(dataLine)
        except Exception, e:
            # print e
            raise e
    if i != 0:
        adc_mean = float(sumSer) / float(i)
    else:
        adc_mean = 0.0
    return adc_mean


def main():
    '''
    # --datatype = int / float
    # --error = 0 / 1
    # --filename = filename
    '''

    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", [
                               "version", "datatype=", "filename=", "error="])

    data_type = 'int'
    error = 0
    filename = ''
    for op, value in opts:
        print op, value
        if op == "-i":
            pass
            # input_file = value
        elif op == "-o":
            pass
            # input_file = value
        elif op == "-h":
            pass
            # input_file = value
        elif op == "--datatype":
            data_type = value
            # input_file = value
        elif op == "--filename":
            filename = value
        elif op == "--error":
            error = value

    filename = filename + '_' + str(time()) + ".csv"
    # filename = "Serial111" + ".csv"
    print filename
    f = open(filename, 'w')  # (1)

    try:
        ser_pressure = serial.Serial(port='COM6', baudrate=2400, timeout=1)
        ser = serial.Serial(port='COM11', baudrate=921600, timeout=1)
    except Exception, e:
        raise e

    while True:
        try:
            dataLine = ser_pressure.read(16)
            # print dataLine
            # hex_show(dataLine)
            # print ser.readline()

            adc_mean_data = adc_data_from_ser(ser, datatype=data_type)
            pressure = hex_resolve(dataLine)
            if error == '1':
                if data_type == 'int':
                    print 'ADC = ', adc_mean_data, '\t',
                elif data_type == 'float':
                    print 's_pressure = ', adc_mean_data, '\t',
                print 'pressure =', pressure, 'error=', (adc_mean_data - pressure)
                f.write(str(pressure) + ',' + str(adc_mean_data) + ',' +
                        str(adc_mean_data - pressure) + "\n")
            else:
                if data_type == 'int':
                    print 'ADC = ', adc_mean_data, '\t',
                elif data_type == 'float':
                    print 's_pressure = ', adc_mean_data, '\t',
                print 'pressure =', pressure
                # print adc_mean_data, pressure
                f.write(str(pressure) + ',' + str(adc_mean_data) + "\n")
        except Exception, e:
            pass
            # print e

    f.close()

if __name__ == '__main__':
    main()
