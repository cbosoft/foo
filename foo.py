import os
import sys

print(f'Python {sys.version}')
print('Running with FOO={} and BAR={}', os.getenv('FOO'), os.getenv('bar'))
