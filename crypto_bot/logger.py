import logging
import os


base_dir = os.path.expanduser('~/Documents/CryptoBotLogs')
if not os.path.exists(base_dir):
    os.mkdir(base_dir)

def make_logger(name):
    path = os.path.join(base_dir, f'{name}.log')
    logger = logging.getLogger()
    logger.setLevel('INFO')
    fmt = '%(asctime)s %(levelname)s\n\t%(message)s'
    fmt = logging.Formatter(fmt)
    fh = logging.FileHandler(path, 'w')
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger
    
