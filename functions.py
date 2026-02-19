from datetime import datetime,timedelta

categorie = {
    "BENZINA":{
        "causali" : ["benzina","benza"],
        "limite" : 140
    },
    "STIPENDIO":{
        "causali" : ["stipendio"],
        "limite" : 1000000
    },
    "CIBO":{
        "causali": ["pizza","sushi","colazione","merenda","gelato","piadina","poke","kfc","mangiare","focaccia","bar","caffe","brioches","tiramisu","frappe","birra","drink","snack"],
        "limite": 110
    },
    "CRYPTO/INVESTIMENTI":{
        "causali": ["crypto","pepe","eth"],
        "limite":1000
    },
    "RIVENDITA/BUSINESS":{
        "causali":["vinted","buoni","puff","sbuff","iphone","PANT JORDAN","PANTALONCINI","POLO RALPH"],
        "limite":200
    },
    "SCOMMESSE":{
        "causali":["scomessa","scommessa","poker","scala","scopa"],
        "limite":0
    },
    "CURA_PERSONALE":{
        "causali":["capelli","medicine","dentifricio","colluttorio","testine","scovolini"],
        "limite":100
    },
    "REGALI":{
        "causali":["regalo","san valentino"],
        "limite":100
    },
    "ABBIGLIAMENTO":{
        "causali":["VESTITI","INTIMO"],
        "limite":80
    },
    "TASSE/FISSO":{
        "causali":["730","ILIAD","BOLLO CARTA"],
        "limite":15
    },
    "ALTRO":{
        "causali":[],
        "limite":0
    }
}

def trova_categoria(a:str):
    a = str(a).lower()#devi mettere DATAFRAME + COLONNA CAUSALE
    for x,y in categorie.items():
        for elemento in y["causali"]:
            if elemento in a:
                return x
    return "ALTRO"


def alert_category(somma_mese):

    for x,y in somma_mese.items():
        if y > categorie[x[1]]["limite"]:
            print( f"\n-ALERT|{x[1]}|{x[0]}\n hai speso:{y}$ | limite:{categorie[x[1]]['limite']}$\n")

def predict_next_month(data_frame):
    date_limit = data_frame["DATA"].max() - timedelta(days=90)
    expense = data_frame[data_frame["DATA"] >=date_limit]
    all_expense = (expense.groupby(["CATEGORIA"])["IMPORTO"].sum() / 3).round(2)
    for x,y in all_expense.items():
            stato =""
            if abs(y) > categorie[x]["limite"]:
                stato ="🔴" 
            else:
                stato = "🟢"
                

            print(f"\n-CATEGORIA |{x}\n Prediction {abs(y)}$ | Limite:{categorie[x]['limite']}$ | {stato}\n")
            













if __name__ == "__main__":

    print("data")
