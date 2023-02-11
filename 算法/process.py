import time
import random
from tqdm import tqdm
from datetime import date

d = date(1996, 10, 1)
with tqdm(total=166, desc='Processing %s'%d.strftime('%Y-%m')) as pbar:
    for i in range(166):
        pbar.set_description("Processing %s"%d.strftime('%Y-%m'))
        time.sleep(random.randrange(0, 3)/10)
        pbar.update(1)
        if d.month == 12:
            d = date(d.year + 1, 1, 1)
        else: d = date(d.year, d.month + 1, 1)