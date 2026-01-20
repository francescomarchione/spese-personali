import pandas as pd

df = pd.ExcelFile("ROUTINE.xlsx")



if __name__ =="__main__":
   df_da_modificare = []
   for sheet in df.sheet_names:
      if "BILANCIO" in sheet:
         foglio_corrente = pd.read_excel("ROUTINE.xlsx",sheet_name=sheet,header=2)
         foglio_corrente["MESE"] = sheet
         tabella_1 = foglio_corrente.loc[:,["DATA","CAUSALE","ENTRATA","USCITA","SALDO","MESE"]]
         tabella_2 = foglio_corrente.loc[:,["DATA.1","CAUSALE.1","ENTRATA.1","USCITA.1","SALDO.1","MESE"]]
         tabella_3 = foglio_corrente.loc[:,["DATA.2","CAUSALE.2","ENTRATA.2","USCITA.2","SALDO.2","MESE"]]
         tabella_2.columns,tabella_3.columns = tabella_1.columns,tabella_1.columns
         for tabella in tabella_1,tabella_2,tabella_3:
            df_da_modificare.append(tabella)

   df_unito = pd.concat(df_da_modificare,ignore_index=True)
   df_unito = df_unito.loc[:, ~df_unito.columns.str.contains("Unnamed")]
   df_pulito = df_unito.dropna(subset =['CAUSALE']).copy()
   df_pulito["ENTRATA"] = pd.to_numeric(df_pulito["ENTRATA"],errors="coerce")
   df_pulito["USCITA"] = pd.to_numeric(df_pulito["USCITA"],errors="coerce")
   df_pulito["IMPORTO"] =  df_pulito["ENTRATA"].fillna(0) - df_pulito["USCITA"].fillna(0)
   somma_mese = df_pulito.groupby("MESE")["IMPORTO"].sum()

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
         "causali":["capelli","medicine""dentifricio","colluttorio","testine","scovolini"],
         "limite":100
      },
      "REGALI":{
         "causali":["regalo","san valentino"],
         "limite":100
      },
      "ABBIGLIAMENTO":{
         "causali":["VESTITI|INTIMO"],
         "limite":80
      },
      "TASSE/FISSO":{
         "causali":["730","ILIAD","BOLLO CARTA"],
         "limite":15
      }

   }






















