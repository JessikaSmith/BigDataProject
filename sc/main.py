#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pandas as pd
import numpy as np
import tqdm
import re
import sys
from matplotlib import pyplot as plt
import seaborn as sns
import math
import matplotlib
from scipy import stats


if __name__ == '__main__':
    types = {'id_str': np.int, 'retweets': np.int, 'reply_to': np.int, 'favorites': np.int, 'replies': np.int}
    parse_dates = ['created_at']
    data = pd.read_csv("../data/twitter.csv", encoding='utf-8', dtype=types, parse_dates=parse_dates)
    print(data.head(10))
    print("Ok")