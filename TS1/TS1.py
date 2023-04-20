# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 07:01:43 2023

Tarea Semanal 1

@author: Fabian Villada
"""

from scipy.signal import TransferFunction
import numpy as np
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

wo = 1

my_tf = TransferFunction([1,-wo],[1,wo])


bodePlot(my_tf, fig_id=1)
pzmap(my_tf, fig_id=2)
GroupDelay(my_tf, fig_id=3)
