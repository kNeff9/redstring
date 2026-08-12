from configparser import ConfigParser
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')

def load_config(filename='database.ini', section='postgresql'):

    # Checking for use of Docker. If so, get env variables instead of .ini. 
    if os.getenv('DB_HOST'):
        return {
            'host': os.getenv('DB_HOST'),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'port': os.getenv('DB_PORT')
        }

    else:

        print("Not docker db")

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