import os
import configparser

def get_confg_file(import_directory):

    ini_array_setup = ['graphing_IOs','graphing_Latency','graphing_lines','graphing_scatter']
    ini_array_config = ['load_type','drives','controller']

    found_ini_file = False
    ini_filename = ''
    config = configparser.ConfigParser()

    for filename in os.listdir(import_directory):
        if filename.endswith(".ini"):
            ini_filename = filename
            found_ini_file = True
            print ini_filename
    if not found_ini_file:
        write_default_ini(import_directory)

        print ('Could not find the .ini config file. Setting up default file. Please check the directory:\n-!- directory -!- {}'
                    .format(import_directory))
        return None

    config.read(import_directory + ini_filename)
    if u'please remove this line and fill in params' in config.sections():
        print('Please check all default parameters and make sure that the configuration file is in the correct order.')
        return None
    #NEED TO CHECK IF ANY SECTIONS OF THE INI FILE ARE BLANK
    print config.sections()
    print 'config setup: {}'.format(config['SETUP']['graphing_IOs'])
    print 'config drives: {}'.format(config['CONFIG']['drives'])

    setup_array = []
    config_array = []

    for string in ini_array_setup:
        setup_array.append(config['SETUP'][string])
    for string in ini_array_config:
        config_array.append(config['CONFIG'][string])
    # print 'setup array: {}'.format(setup_array)
    # print 'config_array: {}'.format(config_array)
    return setup_array, config_array

def write_default_ini(import_directory):
    default_ini_file = import_directory + 'ini_default.ini'
    with open(default_ini_file,'w') as ini:
        ini.write('[please remove this line and fill in params]'+'\n')
        ini.write('\n'+'[SETUP]'+'\n')
        ini.write('graphing_IOs = '+'\n')
        ini.write('graphing_Latency = '+'\n')
        ini.write('graphing_lines = '+'\n')
        ini.write('graphing_scatter = '+'\n')
        ini.write('\n'+'[CONFIG]'+'\n')
        ini.write('load_type = ' + '\n')
        ini.write('drives = ' + '\n')
        ini.write('controller = ' + '\n')