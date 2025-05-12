from datetime import datetime
import re

startDate = datetime(2023, 9, 4)
currentDate = datetime.now()
years = currentDate.year - startDate.year
months = currentDate.month - startDate.month

if months < 0:
    years -= 1
    months += 12

if months == 0:
    years_text = f"{years}"
else:
    years_text = f"{years}.{months}"

try:
    with open("README.md", "r", encoding="utf-8") as file:
        readmeContent = file.read()

    current_pattern = re.compile(re.escape('<!--years_since-->') + '(.*?)' + re.escape('<!--years_since-->'))
    current_match = current_pattern.search(readmeContent)
    current_value = current_match.group(1) if current_match else "non trouvé"

    if current_value != years_text:
        new_content = re.sub(
            re.escape('<!--years_since-->') + '.*?' + re.escape('<!--years_since-->'),
            '<!--years_since-->' + years_text + '<!--years_since-->',
            readmeContent
        )
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(new_content)
    else:
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(readmeContent)
except Exception as e:
    print(f"Erreur lors de la mise à jour du README: {e}")
