# pandas 

## import command

- import pandas

```python
import pandas as pd
```

- read csv file

```python
pd.read_csv([file path])
```

## kaggle Exercise

### Exercise: Explore Your Data

```python 
from datetime import date
# What is the average lot size (rounded to nearest integer)?
avg_lot_size = round(home_data['LotArea'].sum() / home_data['LotArea'].count())

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = date.today().year - home_data['YearBuilt'].max()

# Checks your answers
step_2.check()
```
