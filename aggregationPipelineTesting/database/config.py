from configparser import ConfigParser
import os

def load_config(filename='database.ini', section='postgresql'):

    # Added so database.ini file is able to be found wherever this is ran
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    filepath = os.path.join(base_dir, filename)

    parser = ConfigParser()
    parser.read(filepath)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

if __name__ == '__main__':
    config = load_config()
    print(config)