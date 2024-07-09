from datetime import datetime
import re

startDate = datetime(2023, 9, 4)
currentDate = datetime.now()
years = currentDate.year - startDate.year
months = currentDate.month - startDate.month

if months < 0:
    years -= 1
    months += 12

with open("README.md", "r") as file:
    readmeContent = file.read()

with open("README.md", "w") as file:
    file.write(re.sub(re.escape('<!--years_since-->') + '.*?' + re.escape('<!--years_since-->'), '<!--years_since-->' + f"{years}" if months == 0 else f"{years}.{months}" + '<!--years_since-->', readmeContent))