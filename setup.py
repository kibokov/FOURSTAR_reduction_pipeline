import os
import sys




if __name__ == '__main__': 

    
    os.system('cd pipeline && git clone https://github.com/ysBach/imcombinepy.git && cd imcombinepy $$ python setup.py install')
    os.system('mv -f pipeline/imcombinepy/imcombinepy/ pipeline/temppy')
    os.system('rm -rf pipeline/imcombinepy/')
    os.system('mv pipeline/temppy/ pipeline/imcombinepy')
    

