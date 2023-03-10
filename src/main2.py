from enum import Enum
from pprint import pprint
from tkinter import FIRST
import numpy as np
import random
from sklearn import preprocessing
# from env_virtual import Environment
from env_v2 import Environment

from bp import Algorithm_bp
from exp import Algorithm_exp
# from agent_virtual import Agent

from agent import Agent





"env"
"Normal - Large"
# from set import Setting # here
# from set_large import Setting
from set_large2 import Setting

# from set_mp import Setting


import pprint
from adv import Algorithm_advance
from refer import Property
import pandas as pd

import os
from datetime import datetime




import os
from datetime import datetime
def now_str(str_format='%Y%m%d%H%M'): #image name yyyy/mm/dd
    return datetime.now().strftime(str_format)

result_dir = '/Users/ken/Desktop/before/MP_Large/data/' + now_str(str_format='%Y%m%d_%H%M%S')
os.makedirs(result_dir, exist_ok=True)





def main():

    # Try 10 game.
    result = []
    little = []
    over = []
    goal_count = 0

    # goal_check = 0
    retry_num = []
    goal_y_n = []
    heatmap = [  
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    for epoch in range(1): # 50):

        # heatmap = [  
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # ]


        set = Setting()

        NODELIST, ARCLIST, Observation, map, grid, n_m = set.Infomation()
        # test = [grid, map, NODELIST]
        marking_param = 1
        "Edit"
        test = [grid, map, NODELIST, marking_param     , result_dir] # here

        env = Environment(*test)
        agent = Agent(env, marking_param, *test)
        STATE_HISTORY = []
        CrossRoad = []
        TOTAL_STRESS_LIST = []
        move_cost_result = []
        standard_list = []
        rate_list = []

        VIZL = []
        VIZD = []
        LN = 0
        DN = 0
        backed = []
        goal_check = 0

        print("Env:", env.row_length, env.column_length)


        
        import numpy as np
        test_bp_st = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan     , np.nan, np.nan, np.nan, np.nan]

        "0109 移動した部分"
        # Initialize position of agent.
        state = env.reset()
        phi = [1, 1] # n, m

        # "Add 0129"
        # phi = [0, 1] # n, m
        test_s = 0
        total_stress = 0
        old_to_adavance = "s"
        Backed_just_before = False
        RETRY = False
        "0109 移動した部分"


        "----- Add -----"
        for s in env.states:
            if env.grid[s.row][s.column] == 1:
                goal = s
        size = env.row_length
        map_viz_test = [[0.0 for i in range(size)] for i in range(size)] #known or unknown
        dem = [[0.0 for i in range(size)] for i in range(size)] #2Dgridmap(xw, yw)
        soil = [[0.0 for i in range(size)] for i in range(size)] #2Dgridmap(xw, yw)
        for ix in range(size):
            for iy in range(size):
                map_viz_test[ix][iy] = 1
                # soil[ix][iy] = 1 #sandy terrain
                if dem[ix][iy] <= 0.2:
                    soil[ix][iy] = 1 #sandy terrain
                else:
                    soil[ix][iy] = 0 #hard ground


                # map_viz_test[ix][iy] = 0 # 全マス観測している場合
        "----- Add -----"

        from map_viz import DEMO
        map_viz_init = DEMO(env,     epoch, result_dir)

        UP = 0
        DOWN = 0
        LEFT = 0
        RIGHT = 0 # +1
        DIR = [UP, DOWN, LEFT, RIGHT]
        
        for x in range(6): # +45+50): # 100): # 3 + 3): # +5+5): # +5 + 5     +25): # 6): # RETRYする回数
            print("=================== {} Steps\n===================".format(x))

            # # Initialize position of agent.
            # state = env.reset()
            # RATE = 0.1*x
            RATE = 0.1*x     *0.5




            
            demo = [state, env, agent, NODELIST, Observation, n_m,     map_viz_init] # , reference]
            demo_adv = [state, env, agent, NODELIST, Observation, n_m, RATE,     map_viz_init] # ,          x, weight]
            demo_exp = [state, env, agent, NODELIST, Observation, n_m, RATE,     map_viz_init] # here

            Advance_action = Algorithm_advance(*demo_adv)
            back_position = Algorithm_bp(*demo)
            explore_action = Algorithm_exp(*demo_exp)
            TRIGAR = False
            OBS = []
            # total_stress = 0
            move_step = 0



            "----- Add 0203 -----"
            total_stress = 0
            map_viz_init = DEMO(env,     x*10, result_dir)
            pre_action = None
            exp_find = False # 観測の不確実性

            UP = 0
            DOWN = 0
            LEFT = 0
            RIGHT = 0 # +1
            DIR = [UP, DOWN, LEFT, RIGHT]
            "----- Add 0203 -----"

            "上に移動"
            # "----- Add -----"
            # for s in env.states:
            #     if env.grid[s.row][s.column] == 1:
            #         goal = s
            # size = env.row_length
            # map_viz_test = [[0.0 for i in range(size)] for i in range(size)] #known or unknown
            # dem = [[0.0 for i in range(size)] for i in range(size)] #2Dgridmap(xw, yw)
            # soil = [[0.0 for i in range(size)] for i in range(size)] #2Dgridmap(xw, yw)
            # for ix in range(size):
            #     for iy in range(size):
            #         map_viz_test[ix][iy] = 1
            #         # soil[ix][iy] = 1 #sandy terrain
            #         if dem[ix][iy] <= 0.2:
            #             soil[ix][iy] = 1 #sandy terrain
            #         else:
            #             soil[ix][iy] = 0 #hard ground


            #         # map_viz_test[ix][iy] = 0 # 全マス観測している場合
            # "----- Add -----"

            
            for i in range(200+300): # 4 戻るノードの個数以上は回す

                # total_stress, STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance, GOAL, SAVE_ARC, CrossRoad, Storage, Storage_Stress, TOTAL_STRESS_LIST, move_cost_result, test_bp_st, move_cost_result_X, standard_list, rate_list, map_viz_test, Attribute, Observation, DIR = Advance_action.Advance(STATE_HISTORY, state, TRIGAR, OBS, total_stress, grid, CrossRoad, x, TOTAL_STRESS_LIST, move_step, old_to_adavance, move_cost_result, test_bp_st, Backed_just_before, phi, standard_list, rate_list, test_s, RETRY, map_viz_test, pre_action, DIR)
                total_stress, STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance, GOAL, SAVE_ARC, CrossRoad, Storage, Storage_Stress, TOTAL_STRESS_LIST, move_cost_result, test_bp_st, move_cost_result_X, standard_list, rate_list, map_viz_test, Attribute, Observation, DIR, VIZL, VIZD, LN, DN,     heatmap = Advance_action.Advance(STATE_HISTORY, state, TRIGAR, OBS, total_stress, grid, CrossRoad, x, TOTAL_STRESS_LIST, move_step, old_to_adavance, move_cost_result, test_bp_st, Backed_just_before, phi, standard_list, rate_list, test_s, RETRY, map_viz_test, pre_action, DIR, VIZL, VIZD, LN, DN, backed, exp_find,     heatmap)
                "----- 0130 -----"
                # weight = Attribute
                # print("weight, Attribute:", weight)
                "----- 0130 -----"
                if GOAL:
                    # print("探索済みのノード Storage : {}".format(Storage))
                    # print("未探索のノード CrossRoad : {}".format(CrossRoad))
                    # print("探索終了")
                    break

                RETRY = False
                
                # print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Back position\n============================")

                # total_stress, STATE_HISTORY, state, OBS, BackPosition_finish, TOTAL_STRESS_LIST, move_cost_result, test_bp_st, Backed_just_before, standard_list, rate_list, map_viz_test = back_position.BP(STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance, total_stress, SAVE_ARC, TOTAL_STRESS_LIST, move_cost_result, test_bp_st, move_cost_result_X, standard_list, rate_list, map_viz_test, Attribute)
                total_stress, STATE_HISTORY, state, OBS, BackPosition_finish, TOTAL_STRESS_LIST, move_cost_result, test_bp_st, Backed_just_before, standard_list, rate_list, map_viz_test, VIZL, VIZD, LN, DN, backed,     heatmap = back_position.BP(STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance, total_stress, SAVE_ARC, TOTAL_STRESS_LIST, move_cost_result, test_bp_st, move_cost_result_X, standard_list, rate_list, map_viz_test, Attribute, VIZL, VIZD, LN, DN,     heatmap)


                if BackPosition_finish:
                    BackPosition_finish = False
                    # print(" = 戻り切った状態 🤖🔚 {}回目".format(x+1))
                    
                    "== map, bplist reset =="
                    "== Storageを空にするバージョン =="
                    set = Setting()
                    "Edit"
                    # map = set.reset() # here
                    # test = [grid, map, NODELIST] # , GOAL_STATE]
                    "Edit"
                    test = [grid, map, NODELIST, marking_param, result_dir] # here
                    env = Environment(*test)
                    # agent = Agent(env, *test) # here
                    "Edit"
                    marking_param += 1 # here
                    agent = Agent(env, marking_param, *test)
                    break

                # print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Explore\n============================")
                # RETRY = False

                # total_stress, STATE_HISTORY, state, TRIGAR, CrossRoad, GOAL, TOTAL_STRESS_LIST, move_step, old_to_adavance, phi, standard_list, rate_list, test_s, map_viz_test, pre_action = explore_action.Explore(STATE_HISTORY, state, TRIGAR, total_stress, grid, CrossRoad, x, TOTAL_STRESS_LIST, Backed_just_before, standard_list, rate_list, map_viz_test, DIR)
                total_stress, STATE_HISTORY, state, TRIGAR, CrossRoad, GOAL, TOTAL_STRESS_LIST, move_step, old_to_adavance, phi, standard_list, rate_list, test_s, map_viz_test, pre_action, VIZL, VIZD, LN, DN, exp_find,     heatmap = explore_action.Explore(STATE_HISTORY, state, TRIGAR, total_stress, grid, CrossRoad, x, TOTAL_STRESS_LIST, Backed_just_before, standard_list, rate_list, map_viz_test, DIR, VIZL, VIZD, LN, DN,     heatmap)

                if GOAL:
                    # print("探索済みのノード Storage : {}".format(Storage))
                    # print("未探索のノード CrossRoad : {}".format(CrossRoad))
                    # print("探索終了")
                    break

                # print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Advance\n============================")
                # RETRY = False

            RETRY = True


            # print("Episode {}: Agent gets {} stress.".format(i, total_stress))
            # print("STATE_HISTORY = {}".format(STATE_HISTORY))
            # print("stress = {}".format(TOTAL_STRESS_LIST))
            # print("standard_list = ", standard_list)
            # print("rate_list = ", rate_list)

            # print("Landmark = ", VIZL)
            # print("Goal_Distance = ", VIZD)

            # viz = pd.DataFrame({"Number of Landmarks found":VIZL,
            #         "Distance to goal":VIZD,
            #         })
            # "-----"
            # try:
            #     # print(viz)
            #     # # map_viz_init.viz(viz)
            #     # viz.plot.line(subplots=True, layout=(2, 1), grid=True, figsize=(5, 5)) # , style=['-', '--', '-.', ':'])
            #     # # viz.plot.line(layout=(2, 1), grid=True, figsize=(5, 5))
            #     import matplotlib.pyplot as plt
            #     # # plt.show()
            #     fig = plt.figure(figsize=(5, 5))
            #     ax1 = fig.add_subplot(111)
            #     t = np.linspace(0.0,10.0,1000)
            #     fs = 1.0
            #     ax1.plot(VIZD, 'r-', VIZD, 'k.', alpha = 0.5, label = "Distance to goal")
            #     a=np.arange(len(VIZL))
            #     ax2 = ax1.twinx()
            #     ax2.plot(VIZL, 'b-', VIZL, 'k.', alpha = 0.5, label = "Number of Landmarks found")
            #     h1, l1 = ax1.get_legend_handles_labels()
            #     h2, l2 = ax2.get_legend_handles_labels()
            #     ax1.legend(h1+h2, l1+l2, loc='lower right')
            #     ax1.set_xlabel('Steps')
            #     ax1.set_ylabel("Distance")
            #     ax1.grid(True)
            #     ax2.set_ylabel("Landmark")
            #     plt.show()
            # except:
            #     print("viz エラー")
            "-----"

            # print(len(TOTAL_STRESS_LIST))

            if GOAL:
                print(" {} 回目".format(x+1))
                print("retry : {} 回目".format(x))
                
                # random_test = len(STATE_HISTORY)
                # if random_test <=1290:
                goal_count += 1

                goal_check = 1

                print("⭕️🏁👀🤖🌟 GOAL到達しました!")
                break
        
        if not GOAL:
            print("❌🏁👀🤖🌟 GOAL到達できませんでした!")




        print(heatmap)

        print("Episode {}: Agent gets {} stress.".format(i, total_stress))
        print("STATE_HISTORY = {}".format(STATE_HISTORY))
        print("stress = {}".format(TOTAL_STRESS_LIST))
        print("standard_list = ", standard_list)
        print("rate_list = ", rate_list)

        print("Landmark = ", VIZL)
        print("Goal_Distance = ", VIZD)

        # viz = pd.DataFrame({"Number of Landmarks found":VIZL,
        #         "Distance to goal":VIZD,
        #         })
        # print(len(TOTAL_STRESS_LIST))
        "-----"

        "======== データの出力 ========"
        df = pd.Series(data=STATE_HISTORY)
        df = df[df != df.shift(1)]
        # print('-----削除後データ----')
        # print("Steps:{}".format((len(df))))
        # result.append((len(df)))
        if len(df) <= 45+10: # 100:
            little.append(len(df))

        if len(df) >= 1300: # 100: # 0:
            over.append(len(df))

        print('----- Add 0217 ----')
        print("Steps:{}".format((len(STATE_HISTORY))))
        result.append((len(STATE_HISTORY)))
        print('----- Add 0217 ----')

        goal_y_n.append(goal_check)
        retry_num.append(x) # +1)

    print("==========")
    print("Landmark = ", VIZL)
    print("Goal_Distance = ", VIZD)
    print("steps =", result)
    print("goal_y_n =", goal_y_n)
    print("retry_num =", retry_num)
    # print(result/100)
    print("最小:{}".format(min(result)))
    print("最大:{}".format(max(result)))
    print("45+10 以内 : {}".format(len(little)))
    print("100以上 : {}".format(len(over)))

    print("----------")
    print("試行回数 {}".format(epoch+1))
    print("goal到達回数 : {}".format(goal_count))
    print("到達率 : {}".format(goal_count/(epoch+1)))
    print("----------")

    
    print("x(retry), i : {}, {}".format(x, i))
    Length_history = len(STATE_HISTORY)
    print("length State history: {}".format(Length_history))
    print("length Storage Stress : {}".format(len(TOTAL_STRESS_LIST)))

    #     if len(df) >= 1000:
    #         over.append(len(df))

    # print(result)
    # # print(result/100)
    # print("最小:{}".format(min(result)))
    # print("最大:{}".format(max(result)))
    # print("150 以内 : {}".format(len(little)))
    # print("1000以上 : {}".format(len(over)))
    # print("goal : {}".format(goal_count))
    # print("x(retry), i : {}, {}".format(x, i))
    # Length_history = len(STATE_HISTORY)
    # print("length State history: {}".format(Length_history))
    # print("length Storage Stress : {}".format(len(TOTAL_STRESS_LIST)))

    # # print("standard_list = ", standard_list)
    # # print("rate_list = ", rate_list)


if __name__ == "__main__":
    main()