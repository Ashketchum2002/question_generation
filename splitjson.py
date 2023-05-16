
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

import json
with open('/Users/ashketchum/Downloads/combined-newsqa-data-v1.json', 'r') as f:
    jsondata = json.load(f)

train, test = train_test_split(jsondata)

print(train)
