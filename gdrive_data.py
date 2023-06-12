import gdown
import zipfile
import os

print("Скачивание архива...")
url = 'https://drive.google.com/u/0/uc?id=1JdcY6vHkol2yRItcTe3xKW8vJb48ZYDz'
output = 'registrator.zip'
gdown.download(url, output, quiet=False)
print("Архив скачан...")

print("Распаковка архива...")
fantasy_zip = zipfile.ZipFile('.\\registrator.zip')
fantasy_zip.extractall('.\\')
fantasy_zip.close()
print("Архив распакован!")

print("Удаление архива...") 
path = '.\\registrator.zip'
os.remove(path)
print("Архив удален") 
 
