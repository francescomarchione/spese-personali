
import pandas as pd
import functions as f
from functions import predict_next_month, alert_category, trova_categoria, search_in_category

#carica il file excel e lo salva in una variabile, in questo modo possiamo accedere a tutte le sue sheet

df = pd.ExcelFile("ROUTINE.xlsx")

#carica la sheet "BILANCIO DICEMBRE 25" e la salva in una variabile, in questo modo possiamo accedere a tutte le sue colonne

foglio_corrente = pd.read_excel("ROUTINE.xlsx",
sheet_name="BILANCIO DICEMBRE 25",header=2)

#crea una lista vuota che conterrà tutte le tabelle da modificare, in questo modo possiamo unire tutte le tabelle in un unico dataframe


df_da_modificare = []

#ciclo che scorre tutte le sheet del file excel e salva in una variabile tutte le tabelle da modificare, in questo modo possiamo unire tutte le tabelle in un unico dataframe

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

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

df_unito = pd.concat(df_da_modificare,ignore_index=True)

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

df_unito = df_unito.loc[:, ~df_unito.columns.str.contains("Unnamed")]

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

df_pulito = df_unito.dropna(subset =['CAUSALE']).copy()

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

df_pulito["ENTRATA"] = pd.to_numeric(df_pulito["ENTRATA"],errors="coerce")

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

df_pulito["USCITA"] = pd.to_numeric(df_pulito["USCITA"],errors="coerce")

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

df_pulito["IMPORTO"] =  df_pulito["ENTRATA"].fillna(0) - df_pulito["USCITA"].fillna(0)
df_pulito["CATEGORIA"] = df_pulito["CAUSALE"].apply(f.trova_categoria)

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

df_pulito["DATA"] = pd.to_datetime(df_pulito["DATA"],errors="coerce")

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

somma_mese = df_pulito.groupby(["MESE","CATEGORIA"])["IMPORTO"].sum()

#creazione di un dizionario con le categorie e le causali associate, oltre al limite di spesa per ogni categoria

alert = df_pulito.groupby(["MESE","CATEGORIA"])["IMPORTO"].sum().unstack().fillna(0)




if __name__ =="__main__":
    #alert_category(somma_mese)
    #print(alert_category(somma_mese))
    #print(predict_next_month(df_pulito))
    #print(somma_mese)
    search_in_category(df_pulito, "BILANCIO FEBBRAIO 26", "BENZINA")
    
