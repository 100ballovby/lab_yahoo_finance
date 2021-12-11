import os
import json
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from datetime import datetime

KEY = os.environ.get('API_KEY')
HOST = os.environ.get('API_HOST')

symbol_string = ''
data = {}

