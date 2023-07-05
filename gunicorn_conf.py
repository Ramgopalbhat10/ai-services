import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'info'
accesslog = '-'  # stdout
errorlog = '-'  # stderr