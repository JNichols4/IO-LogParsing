import pandas as pd
import numpy as np
import os

def generate_graph_scatter(output_directory, device_array, data_series, graph_type='scatter',startvar=0, stopvar=11):
    # Some sample data to plot.
    # Plot the IO of the drives

    if startvar==0:
        controller_type='controller_a'
    else:
        controller_type='controller_b'

    excel_file_scatter = output_directory + 'scatter_{}.xlsx'.format(controller_type)
    writer = pd.ExcelWriter(excel_file_scatter, engine='xlsxwriter')

    for iterator_count in range(startvar, stopvar):
        data_dict = {'IOs/s':{},'Latency':{}}
        list_data = []
        time_data = []

        for i in range(len(data_series[iterator_count])):
            if (i%2)==0:
                try:
                    data_s = float(data_series[iterator_count][i])
                    list_data.append(data_s)
                except ValueError:
                    list_data.append(0)
            else:
                try:
                    data_s = float(data_series[iterator_count][i])
                    time_data.append(data_s)
                except ValueError:
                    time_data.append(0)

        #print list_data, time_data
        data_dict['IOs/s'] = list_data
        data_dict['Latency'] = time_data
        #print data_dict

        # Create a Pandas dataframe from the data.
        df = pd.DataFrame(data=data_dict)

        sheet_string = 'Sheet'+str(iterator_count)
        device_string = device_array[iterator_count%12]

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        sheet_name = sheet_string
        df.to_excel(writer, sheet_name=sheet_name)

        # Access the XlsxWriter workbook and worksheet objects from the dataframe.
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Create a chart object.
        chart = workbook.add_chart({'type': graph_type})

        # Configure the series of the chart from the dataframe data.

        chart.add_series({
            'categories': [sheet_string, 1, 1, len(list_data), 1],
            'values':     [sheet_string, 1, 2, len(time_data), 2],
        })

        # Configure the chart axes.
        chart.set_title({'name': device_string})
        chart.set_x_axis({'name': 'IOs/s', 'position_axis': 'on_tick'})
        chart.set_y_axis({'name': 'Latency', 'major_gridlines': {'visible': False}})

        # Turn off chart legend. It is on by default in Excel.
        chart.set_legend({'position': 'none'})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('D2', chart)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

def generate_graph_line_IOs(output_directory, device_array, data_series, controller, graph_type='line', startvar=0, stopvar=11):

    controller_type = 'controller_{}'.format(controller)

    excel_file_line = output_directory + 'line_IOS_{}.xlsx'.format(controller_type)

    writer = pd.ExcelWriter(excel_file_line, engine='xlsxwriter')

    for iterator_count in range(startvar, stopvar):
        list_data = []
        for i in range(len(data_series[iterator_count])):
            if (i%2)==0:
                try:
                    data_s = float(data_series[iterator_count][i])
                    list_data.append(data_s)
                except ValueError:
                    list_data.append(0)

        min_y_axis = 10000
        #min_y_axis = min(list_data)-500
        max_y_axis = 14000
        #max_y_axis = max(list_data)+500

        # Create a Pandas dataframe from the data.
        df = pd.DataFrame(data=list_data)

        sheet_string = 'Sheet'+str(iterator_count)
        device_string = device_array[iterator_count%12]

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        sheet_name = sheet_string
        df.to_excel(writer, sheet_name=sheet_name)

        # Access the XlsxWriter workbook and worksheet objects from the dataframe.
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Create a chart object.
        chart = workbook.add_chart({'type': graph_type})

        # Configure the series of the chart from the dataframe data.

        chart.add_series({
            'categories': [sheet_string, 1, 0, len(list_data), 0],
            'values':     [sheet_string, 1, 1, len(list_data), 1],
        })

        # Configure the chart axes.
        chart.set_title({'name': device_string})
        chart.set_x_axis({'name': 'Minutes', 'position_axis': 'on_tick'})
        chart.set_y_axis({'name': 'IOs/s', 'major_gridlines': {'visible': False},'min': min_y_axis,'max': max_y_axis})

        # Turn off chart legend. It is on by default in Excel.
        chart.set_legend({'position': 'none'})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('D2', chart)

    #save and close the workbook
    writer.save()

def generate_graph_line_Latency(output_directory, device_array, data_series, controller, graph_type='line', startvar=0, stopvar=11):

    controller_type = 'controller_{}'.format(controller)

    excel_file_line = output_directory + 'line_Latency_{}.xlsx'.format(controller_type)

    writer = pd.ExcelWriter(excel_file_line, engine='xlsxwriter')

    for iterator_count in range(startvar, stopvar):
        list_data = []
        for i in range(len(data_series[iterator_count])):
            if (i%2)==1:
                try:
                    data_s = float(data_series[iterator_count][i])
                    list_data.append(data_s)
                except ValueError:
                    list_data.append(0)

        min_y_axis = 0
        #min_y_axis = min(list_data)-500
        max_y_axis = max(list_data)+5
        #max_y_axis = max(list_data)+500

        # Create a Pandas dataframe from the data.
        df = pd.DataFrame(data=list_data)

        sheet_string = 'Sheet'+str(iterator_count)
        device_string = device_array[iterator_count%12]

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        sheet_name = sheet_string
        df.to_excel(writer, sheet_name=sheet_name)

        # Access the XlsxWriter workbook and worksheet objects from the dataframe.
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Create a chart object.
        chart = workbook.add_chart({'type': graph_type})

        # Configure the series of the chart from the dataframe data.

        chart.add_series({
            'categories': [sheet_string, 1, 0, len(list_data), 0],
            'values':     [sheet_string, 1, 1, len(list_data), 1],
        })

        # Configure the chart axes.
        chart.set_title({'name': device_string})
        chart.set_x_axis({'name': 'Minutes', 'position_axis': 'on_tick'})
        chart.set_y_axis({'name': 'Latency', 'major_gridlines': {'visible': False},'min': min_y_axis,'max': max_y_axis})

        # Turn off chart legend. It is on by default in Excel.
        chart.set_legend({'position': 'none'})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('D2', chart)

    #save and close the workbook
    writer.save()