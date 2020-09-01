#Importacao dos recursos necessarios
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

#fim da importacao
robo = ChatBot('BOT')
arq = open('gramatica2.txt').read()
lista = arq.strip().split("\n")

#arquivo = open("D:\LTP.txt", 'r')
apr1 = ['oi','opa', 'Tudo bem?', 'Vai indo','Como vai você?','estou bem',"qual a sua duvida?", 'bem','Em que posso ser util?', 'bem', 'Em que posso ajudar ?', 'indo','Em que posso ser util?',
            'indo', 'Em que posso ajudar ?', 'como vai voce?', 'Eu estou bem, em que posso ajudar ?',
            'que bom', 'Sim, em oque mais posso ajudar ?' , 'Que bom', 'Sim, em oque mais posso ajudar?', 'Sim, eu tenho uma pergunta.', 'Qual é a sua pergunta?',
            'sim eu tenho uma pergunta','Qual é a sua pergunta?', 'o que é um verbo?', 'Bem, verbo é uma palavra com a qual se afirma a existência de ação, estado ou\
            fenômeno da natureza. Por exemplo: Você gosta de mim. Nesta frase o verbo é a\
            palavra gostar. Então, qual é o verbo da frase Maria estuda muito? Você sabe?' , 'estuda', 'Muito bem!', 'o que é uma gramática? ', 'Gramática designa um conjunto de regras que regem o uso de uma língua,\
            especialmente o modo como as unidades desta se combinam entre si para formar unidades maiores.', 'Legal' ,'Tem mais alguma pergunta?' , ' o que é um substantivo?',
            'Bem, tudo que existe é ser e todo ser tem um nome, certo? Um substantivo é uma palavra que denomina um ser']

treinamento = ChatterBotCorpusTrainer(robo)

treinamento.train(
"chatterbot.corpus.Portuguese",
"chatterbot.corpus.Portuguese.linguistic_knowledge")

trainer = ListTrainer(robo)
trainer.train(apr1)
trainer.train(lista)
#treinamento.export_for_training('./ppp.json')
while True:
    pergunta = input("Usuario: ")
    resposta = robo.get_response(pergunta)
    if float(resposta.confidence)>0.3:
        print ('BOT: ', resposta)
    else:
        print ('BOT: Ixi, não sei te responder essa questão')
   


