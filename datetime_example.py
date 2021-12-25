from datetime import datetime

ts = 1638801000
dt = datetime.fromtimestamp(ts)
raw_data = dt.strftime('%d/%m/%Y')
print(raw_data)


