import re

def itemize(string):
    #creates an array from columns in a string (based off whitespace)
    item_string = re.sub("\s+",",",string.strip())
    #print item_string
    item_array = item_string.split(',')
    return item_array

def ddp(device):
    # short for develop device position. returns an integer used to iterate through the device array
    dr_num = device[6:8]
    integer_val = int(dr_num,16)
    return integer_val

def convert_response_time(input_string):
    if any(string in input_string for string in ['m', 'u']):
        if 'm' in input_string:
            resp_string = input_string.replace('m', '')
            resp_int = float(resp_string)
        else:
            resp_string = input_string.replace('u', '')
            resp_int = float(resp_string) * .001 #converts to milliseconds
    else:
        resp_int = 'N/A cnp'
    return resp_int

def split_io_parsing(import_file, drive_array, drives, controller):
    raw_device_array = []
    drives_in_log = drives
    check_bool = 0
    line_number = 1
    data_check = 0
    for line in import_file:
        if 'ID    Device' in line:
            check_bool = 1
        if check_bool == 1:
            if '#' in line:
                if not any(string in line for string in ['seconds', 'ramp', 'begin', 'device']):  # ['seconds','ramp','begin','device'] not in line:
                    line_array = itemize(line)
                    # print "running data -!- line: {}, device: {}, IOs/s: {}, mrt: {}".format(line_number, line_array[1], line_array[10], line_array[8])
                    device, io_data, resp_string = line_array[1], line_array[10], line_array[8]
                    resp_int = convert_response_time(line_array[8])
                    pos = ddp(device)%drives_in_log
                    drive_array[pos].append(io_data)
                    drive_array[pos].append(resp_int)
                    if device not in raw_device_array:
                        raw_device_array.append(device)
                elif 'ramp' in line:
                    # print "Passing the ramp start sequence..."
                    if data_check != 0:
                        data_check = 0
                elif 'test' in line:
                    # print "Passing the test start sequence..."
                    if data_check != 1:
                        data_check = 1
                elif all(string in line for string in ['device', 'complete']):
                    line_array = itemize(line)
                    # print line_array
                    # print "complete data -!- line: {}, device: {}, IOs/s: {}, mrt: {}".format(line_number, line_array[1], line_array[10],line_array[21])
                    device, io_data, resp_data = line_array[2], line_array[11], line_array[21]
                    resp_int = convert_response_time(line_array[21])
                    pos = ddp(device)%drives_in_log
                    drive_array[pos].append(io_data)
                    drive_array[pos].append(resp_int)
        line_number += 1
    device_array = sorted(raw_device_array)
    return drive_array, device_array

def parallel_io_parsing(import_file, drive_array, drives, controller):
    if controller=='b':
        offset = drives
    else:
        offset = 0
    raw_device_array = []
    check_bool = 0
    line_number = 1
    data_check = 0
    for line in import_file:
        if 'ID    Device' in line:
            check_bool = 1
        if check_bool == 1:
            if '#' in line:
                if not any(string in line for string in ['seconds', 'ramp', 'begin', 'device']):  # ['seconds','ramp','begin','device'] not in line:
                    line_array = itemize(line)
                    # print "running data -!- line: {}, device: {}, IOs/s: {}, mrt: {}".format(line_number, line_array[1], line_array[10], line_array[8])
                    device, io_data, resp_string = line_array[1], line_array[10], line_array[8]
                    resp_int = convert_response_time(line_array[8])
                    pos = (ddp(device)%drives)+offset
                    drive_array[pos].append(io_data)
                    drive_array[pos].append(resp_int)
                    if device not in raw_device_array:
                        raw_device_array.append(device)
                elif 'ramp' in line:
                    # print "Passing the ramp start sequence..."
                    if data_check != 0:
                        data_check = 0
                elif 'test' in line:
                    # print "Passing the test start sequence..."
                    if data_check != 1:
                        data_check = 1
                elif all(string in line for string in ['device', 'complete']):
                    line_array = itemize(line)
                    # print line_array
                    # print "complete data -!- line: {}, device: {}, IOs/s: {}, mrt: {}".format(line_number, line_array[1], line_array[10],line_array[21])
                    device, io_data, resp_data = line_array[2], line_array[11], line_array[21]
                    resp_int = convert_response_time(line_array[21])
                    pos = (ddp(device)%drives)+offset
                    drive_array[pos].append(io_data)
                    drive_array[pos].append(resp_int)
        line_number += 1
    device_array = sorted(raw_device_array)
    return drive_array, device_array

def odds_and_evens_parsing():
    return 0

def check_parsing_type(type_string, drives, controller):
    string_array = ['split','parallel','odds and evens']
    #assumes that the string must not be in unix format
    if any(string in type_string for string in string_array):
        print('Parsing type found: {}'.format(type_string))
        if type_string is 'split':
            modifier = 1
    else:
        print('Unrecognized parsing type string. Please check the .ini file.\nMake sure that the string'
              'is one of these options: {}'.format(string_array))

