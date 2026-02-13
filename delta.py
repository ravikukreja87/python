from datetime import date , timedelta  
import random

d1,d2=date(2020,3,4),date(2025,5,6)

print(d1+timedelta(days=random.randint(0, (d2-d1).days)))
