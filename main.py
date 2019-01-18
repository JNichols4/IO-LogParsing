import os
import time
import re
import graphing_pandas as gp
import grab_defaults as gd
import parsing

controller = 'a'
import_directory = os.getcwd() + "\\logs\\1-10-19\\"
import_filename = import_directory + 'bmpio1.txt' #'ctrl {} baseline teraterm (notime).log'.format(controller)

output_directory = os.getcwd() + "\\logs\\parsed\\1-10-19\\"
output_filename_io = output_directory + 'bmpio1_parsed_io.csv' #'ctrl {} baseline teraterm.csv'.format(controller)
output_filename_response_time = output_directory + 'bmpio1_parsed_resp.csv' #'ctrl {} baseline teraterm drive response times.csv'.format(controller)
output_filename_scatter = output_directory + 'bmpio1_parsed_scatter.csv' #'ctrl {} baseline teraterm combined data.csv'.format(controller)

#print import_filename
import_file = open(import_filename,"r")

#count the number of devices, 0 -> n

def status(msg_string):
    print(msg_string)

def parse_string(start, stop, string):
    device = string[4:12].strip()
    data = string[start:stop].strip()
    return device, data

def write_device_list(filename, device_array, spacing=0):
    for i in range(len(device_array)):
        filename.write(device_array[i]+',')
        if spacing>0:
            for x in range(spacing):
                filename.write(' ' + ',')
    filename.write('\n')

def create_device_array(number_of_drives):
    drive_array = []
    for i in range(number_of_drives):
        drive_array.append([])
    return drive_array

def generate_graphs(setup_array,output_directory,device_array,data_series,drives,controller):
    if int(setup_array[0])==1:
        #just IOs
        gp.generate_graph_line_IOs(output_directory, device_array, data_series, controller, stopvar=drives)
    if int(setup_array[1])==1:
        #specifically Latency
        gp.generate_graph_line_Latency(output_directory,device_array,data_series,controller,stopvar=drives)
    if int(setup_array[2])==1:
        #lines
        return 0
    if int(setup_array[3])==1:
        #scatter
        return 0


try:
    # ini_array_setup = ['graphing_IOs', 'graphing_Latency', 'graphing_lines', 'graphing_scatter']
    # ini_array_config = ['load_type', 'drives']
    setup_array, config_array = gd.get_config_file(import_directory)
    controller = config_array[2]
    print 'Setup Array: ', setup_array
    print 'Config Array: ', config_array
    print (str(config_array[0]))
    if str(config_array[0])=='split':
        d_nums = int(config_array[1])/2
        device_array_empty = create_device_array(d_nums)
        drive_array, device_array = parsing.split_io_parsing(import_file, device_array_empty, d_nums, controller)
        generate_graphs(setup_array,output_directory,device_array,drive_array,d_nums,controller)
        #print 'Drive array: {}\nDevice array: {}'.format(drive_array,device_array)
    '''
    if str(config_array[0])=='parallel':
        for string in ['a','b']:
            controller = string
            d_nums = int(config_array[1])*2
            device_array_empty = create_device_array(d_nums)
            if string is 'a':
                #length of 2*number_of_drives
                drive_array_a, device_array = parsing.parallel_io_parsing(import_file, device_array_empty, config_array[1], controller)
            else:
                drive_array, device_array = parsing.parallel_io_parsing(import_file, drive_array_a, config_array[1], controller)
    '''


except TypeError:
    print('Exiting...')
    exit(0)





#generates a graph of Latency vs IOs/s
output_file_io = open(output_filename_io,'w')
output_file_resp = open(output_filename_response_time,'w')
output_file_scatter = open(output_filename_scatter,'w')

'''
if len(drive_array[0])>0:
    lengthvar = len(drive_array[0])
    startvar = 0
    stopvar = 11
    write_device_list(output_file_io,device_array)
    write_device_list(output_file_resp,device_array)
    write_device_list(output_file_scatter,device_array, spacing=1)
    #gp.generate_graph_scatter(output_directory, device_array, drive_array)
    gp.generate_graph_line(output_directory, device_array, drive_array)
else:
    lengthvar = len(drive_array[12])
    startvar = 12
    stopvar = 23
    write_device_list(output_file_io,device_array)
    write_device_list(output_file_resp,device_array)
    write_device_list(output_file_scatter,device_array)
    #gp.generate_graph_scatter(output_directory, device_array, drive_array, startvar=startvar, stopvar=stopvar)
    gp.generate_graph_line(output_directory, device_array, drive_array, startvar=startvar, stopvar=stopvar)



for i in range(lengthvar):

    if ((i%200)==0 and i!=0):
        output_file_io.write('\n')
        output_file_resp.write('\n')
        write_device_list(output_file_io, device_array)
        write_device_list(output_file_resp, device_array)
        write_device_list(output_file_scatter, device_array, spacing=1)

    if (i%2) == 0:
        for j in range(startvar,stopvar+1):
            #print str(drive_array[i][j])
            output_file_io.write(str(drive_array[j][i])+',')
            output_file_scatter.write(str(drive_array[j][i]) + ',' + str(drive_array[j][i+1]) + ',')
        output_file_io.write('\n')
        output_file_scatter.write('\n')
    else:
        try:
            for j in range(startvar,stopvar+1):
                output_file_resp.write(str(drive_array[j][i])+',')
                #output_file_scatter.write(str(drive_array[j][i])+','+str(drive_array[j][i+1])+',')
            output_file_resp.write('\n')
            #output_file_scatter.write('\n')
        except IndexError:
            print 'Completed the sequence!'


try:
    os.startfile(output_filename_io)
except IOError:
    print 'File already open, processing other files...'
try:
    os.startfile(output_filename_response_time)
except IOError:
    print 'File already open, processing other files...'
try:
    os.startfile(output_filename_scatter)
except IOError:
    print 'File already open, processing other files...'
'''