import os
import random
import re
import sys
import sqlite3

import linearmodels 
import numpy as np
import pandas as pd
import scipy as sp
import statsmodels.api as sm
import statsmodels.formula.api as smf

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
from vega_datasets import data

# pandas settings
pd.set_option('display.max_rows', 120)
pd.set_option('display.max_columns', 120)
pd.set_option('max_colwidth', None)
pd.set_option('precision', 4)

# seaborn settings
sns.set_context("notebook")
# sns.set(rc={'figure.figsize': (16, 9.)})
sns.set_style("whitegrid")

# global vars
TEMPDIR = '/Users/fgu/tmp/'
SAMPLEDATA = '/Users/fgu/tmp/data_777.parquet'