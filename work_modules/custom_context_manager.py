from time import time
from datetime import datetime


class CustomTimerContextManager:
    def __init__(self, function, name: str = 'logs.csv', flags='a+', ):
        self.my_file = open(f'{name}', flags)
        self.function = function

    def __enter__(self):
        self.starttime = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        running_time = time() - self.starttime

        base_str = f'''The function was called:;{self.function};Time the script was executed:;{datetime.now()};\
Execution time (sec):;{running_time};status:;'''

        if exc_type is None:
            self.my_file.write(f'{base_str}success\n')
        elif exc_type is TypeError:
            self.my_file.write(f'{base_str}Error: TypeError\n')
        elif exc_type is FileNotFoundError:
            self.my_file.write(f'{base_str}Error: FileNotFoundError\n')
        else:
            print(exc_type)
            self.my_file.write(f'{base_str}Error: there was unexpected error\n')

        self.my_file.close()

        ''' if function returns False (or without return at all), than processing is transferred to the \
        highest level and errors can destroy the running of the program. In case if it returns True \
        we do not transfer errors to another level 
        '''
        return True


if __name__ == "__main__":
    pass
