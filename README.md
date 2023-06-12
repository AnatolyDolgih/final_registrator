# __Проект "Регистратор"__

## __1. Инструкция по установке__

1. Необходимо склонировать текущий репозиторий в папку своего проекта: перейти в каталог, где будет лежать проект и выполнить команду:  
   ```git clone https://github.com/AnatolyDolgih/final_registrator.git```  
   (если не установлена утилита git, то ее следует установть - [инструкция](https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git))
2. Далее спускаемся в каталог ./final_registrator и установливаем виртуальное окружение и активируем его:  
   ```python -m venv .env```  
   ```\.env\Scripts\activate```  
3. Выполнить команду  
   ```pip install -r requirements.txt```  
   (данная команда усатновит зависимости)
4. Запускаем скрипт gdrive_data.py с помощью команды  
   ```python gdrive_data.py```  
   В качестве альтернативы можно распаковать там архив с моделями и данными вручную - [архив](https://drive.google.com/file/d/1JdcY6vHkol2yRItcTe3xKW8vJb48ZYDz/view?usp=sharing) (ВАЖНО! путь до каталогов models и data должен быть ./registrator/models и ./registrator/data соответственно)
