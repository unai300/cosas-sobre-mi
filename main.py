print("hola")
meme_dict = { "CRINGE": "Algo excepcionalmente raro embarazoso", "LOL": "Una respuesta común a algo gracioso",}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
for i in range(5):
    if word in meme_dict.keys():
         print(meme_dict[word])   
    else:
         print("no se encontro la palabra")
