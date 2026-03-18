from datetime import datetime,timedelta
from unicodedata import category
#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

categorie = {
    "BENZINA":{
        "causali" : ["benzina","benza"],
        "limite" : 160
    },
    "STIPENDIO":{
        "causali" : ["stipendio"],
        "limite" : 1000000
    },
    "CIBO":{
        "causali": ["pizza","sushi","colazione","merenda","gelato","piadina","poke","kfc","mangiare","focaccia","bar","caffe","brioches","tiramisu","frappe","birra","drink","snack"],
        "limite": 100
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
        "limite":70
    },
    "REGALI":{
        "causali":["regalo","san valentino"],
        "limite":75
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

def trova_categoria(a:str):#funzione che prende in input una causale e restituisce la categoria a cui appartiene, se non appartiene a nessuna categoria restituisce "ALTRO"

    a = str(a).lower()#devi mettere DATAFRAME + COLONNA CAUSALE
    for x,y in categorie.items():
        for elemento in y["causali"]:
            if elemento in a:
                return x
    return "ALTRO"

#funzione che prende in input la somma per mese e categoria e stampa un alert se la spesa supera il limite

def alert_category(somma_mese):
    for x,y in somma_mese.items():
        if y > categorie[x[1]]["limite"]:
            print( f"\n-ALERT|{x[1]}|{x[0]}\n hai speso:{y}$ | limite:{categorie[x[1]]['limite']}$\n")

#funzione che prende in input il dataframe pulito e predice la spesa per il prossimo mese basandosi sulla media degli ultimi 3 mesi

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

#funzione che prende in input il mese e la categoria e stampa tutte le causali associate a quella categoria per quel mese
def search_in_category(df_pulito, file_mese, category):
    # Filtro per mese
    df_mese = df_pulito[df_pulito["MESE"] == file_mese]
    # Filtro anche per categoria
    df_filtrato = df_mese[df_mese["CATEGORIA"] == category]

    # Ora cicla sul DataFrame filtrato, non sul dizionario
    for indice, riga in df_filtrato.iterrows():
        print(f"\n-CAUSALE | {riga['CAUSALE']} | {riga['USCITA']}$")
    print(f"\n-----------------------------------------\n-TOTALE | {df_filtrato['USCITA'].sum()}$\n-----------------------------------------\n")
   


if __name__ == "__main__":

    print("data")
