from datetime import datetime
import re

startDate = datetime(2023, 9, 4)
currentDate = datetime.now()
years = currentDate.year - startDate.year
months = currentDate.month - startDate.month

if months < 0:
    years -= 1
    months += 12
try:
    with open("README.md", "r", encoding="utf-8") as file:
        readmeContent = file.read()

    new_content = re.sub(
        re.escape('<!--years_since-->') + '.*?' + re.escape('<!--years_since-->'),
        '<!--years_since-->' + years_text + '<!--years_since-->',
        readmeContent
    )

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"README mis à jour avec succès: {years_text} an(s) depuis l'inscription")
except Exception as e:
    print(f"Erreur lors de la mise à jour du README: {e}")
