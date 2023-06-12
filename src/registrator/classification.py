""" Данный модуль реализует функционал классификатора"""

import os
import torch 
import params as p
from transformers import AutoTokenizer

pathToModels = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../models/'))
pathToData = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/'))

class Classificator():
    
    def __init__(self) -> None:
        print("Создание классификатора...")
        self.category = p.categories_dict
        self.model = torch.load(pathToModels + "\\intent_catcher.pt", map_location=torch.device('cpu'))
        self.tokenizer = AutoTokenizer.from_pretrained('DeepPavlov/rubert-base-cased-sentence')
        print("Модель классификатора загружена")
        
    def name_classification(self, text : str) -> bool:
        """ФИО классифиакция
        
        Определяет, является ли полученная реплика ФИО, или нет

        Args:
            text (str): входящая реплика пользователя

        Returns:
            bool: результат классификации
        """
        fio = text.split(" ")
        for l in fio:
            f = open(pathToData + "\\male_name.txt", "r", encoding = 'utf-8')
            for line in f:
                a = line.strip().lower()
                if (l == a):
                    f.close()
                    return True
            
            f = open(pathToData + "\\female_name.txt", "r", encoding = 'utf-8')
            for line in f:
                a = line.strip().lower()
                if (l == a):
                    f.close()
                    return True
        return False
    
    def bin_classification(self, text : str) -> bool:
        """Бинарная классификация
        
        Определяет, относится ли данная реплика к теме заселения в отель
        или к свободной теме.

        Args:
            text (str): входящая реплика пользователя

        Returns:
            bool: True - реплика о заселении в отель
                  False - реплика на свободную тему
        """
        text = text.lower().rstrip().lstrip()
        count = 0
        for i in p.reg_word:
            if (text.find(i) >= 0):
                count += 1
        if (count > 0):
            return True
        else:
            return False
    
    def intent_classification(self, text : str) -> str:
        """Классификация намерения

        Args:
            text (str): реплика пользователя

        Returns:
            str: категория высказывания (ключ к словарю)
        """
        model_input = self.tokenizer.encode(text, return_tensors='pt')
        model_output = self.model.bert.config.id2label[self.model(model_input)['logits'].argmax().item()]
        return str(model_output)
      
    def classify(self, text : str) -> int:
        """Итоговая классификация реплики

        Args:
            text (str): реплика пользователя

        Returns:
            int: категория высказывания
        """
        # проверяем фио
        if(self.name_classification(text)):
            return self.category["fio"]
        
        text = text.lower().lstrip().rstrip()
        # проверяем, какой у нас диалог
        if(not self.bin_classification(text)):
            return self.category["free_dialog"]
        
        return self.category[self.intent_classification(text)]
        
if __name__ == "__main__":
    print(__doc__)