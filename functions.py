
categorie = {
    "BENZINA":{
        "causali" : ["benzina","benza"],
        "limite" : 140
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
        "causali":["vinted","puff","sbuff","iphone","PANT JORDAN","PANTALONCINI","POLO RALPH"],
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
    }

}

def trova_categoria(a:str):
    a = str(a).lower()
    for x,y in categorie.items():
        for elemento in y["causali"]:
            if elemento in a:
                return x
    return "ALTRO"

def alert_categoria(somma_mese):
    for x,y in somma_mese.items():
        for categoria,limite in categorie.items():
            if y >= limite["limite"]:
                print("\nALERTTTTTT!!!!\n")
                return f"in{x,y}MAGGIORE DI {categorie['limite']}"
        else:
            print("\nOK\n")
            return f"in{x,y}MINORI DI {categorie['limite']}"



if __name__ == "__main__":
    print(trova_categoria("pizza"))
    print(categorie.values())
