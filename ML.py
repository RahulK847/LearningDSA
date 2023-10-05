import random
import pandas as pd
import numpy as np
np.random.seed()
data = {
    "Roll No:":[2101790, 2101791,2101792,2101793,2101794],
    "English":np.random.randint(100, size=5),
    "Maths":np.random.randint(100, size=5),
    "Hindi":np.random.randint(100, size=5),
    "Biology":np.random.randint(100, size=5)
}
print(pd.DataFrame(data))
