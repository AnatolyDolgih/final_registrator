import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './registrator/')))
import registrator.classification as cls
import registrator.generation as gn

classificator = cls.Classificator()
gen = gn.Generator()

def post_process(replic):
    text = str(replic)
    text = text.lstrip().rstrip().capitalize()
    text = text.replace(" .", ".")
    text = text.replace(" ,", ",")
    text = text.replace(" !", "!")
    text = text.replace(" ?", "?")
    return text

while True:
    print("Введите реплику пользователя:")
    data = input()
    
    category = classificator.classify(str(data))
    answer = gen.generate(str(data), category)
    answer = post_process(answer)
    print(answer)