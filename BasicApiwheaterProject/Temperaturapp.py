import dotenv
import os
import requests as R
import pandas
#Pegar a chave da api, adicionar as informações de busca de temperatura e de local, depois acessar elas em uma planilha excel através do pandas
    
def temperatura_locais():
    print("Buscando clima")   
    dotenv.load_dotenv()
    chave = os.getenv("CHAVE_PESSOAL")
    print(chave)
    #-- Peguei a chave, preciso adicionar as informaçoes de onde tenho que pegar o clima
    cidade = "Rio de janeiro"
    URL_cidade = f"http://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={chave}&units=metric"
    catar_info = R.get(URL_cidade)
    if catar_info.status_code == 200:
        print("Conexão feita com sucesso!")
        dados_json = catar_info.json()
        lista_previsao = dados_json["list"]
        print(len(lista_previsao))
        lista_csv = [] #Criei uma lista para adicionar cada previsao do dicionario e transformar em um Dataframe para levar os dados para a planilha
        for i in lista_previsao:  #Fiz um loop pra buscar cada previsao num espaço de tempo futuro
            data_exata = i["dt_txt"]
            temperatura = i["main"]["temp"]
            lista_csv.append({"Data": data_exata, "Temp" : temperatura})
        tabela = pandas.DataFrame(lista_csv) 
        tabela.to_csv("Previsao_Rio_de_janeiro.csv",index = False) #Joguei os dados para a planilha e criei ela
        media = tabela["Temp"].mean()
        print(f"Temperatura media do Estado : {media:.2f}")
    elif  catar_info.status_code == 401 or catar_info.status_code == 404:
        print("Error")
temperatura_locais() #Rodar a api 

