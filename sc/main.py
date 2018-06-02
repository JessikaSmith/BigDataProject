#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pandas as pd
import numpy as np
import datetime, time
from sc.CONFIG import *


if __name__ == '__main__':
    upd_columns = {'id_str': 'id',
                   'screename': 'username',
                   'created_at': 'date_time',
                   'pic': 'picture'}
    raw_data = pd.read_csv(CONFIG.RAW_DATA_PATH, encoding='utf-8', parse_dates=['created_at', 'creation']).drop(
        "Unnamed: 0",
        axis=1)
    raw_data.rename(columns=upd_columns, inplace=True)
    print("OK")
