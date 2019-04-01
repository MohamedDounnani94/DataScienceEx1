import numpy
import pandas as pd
import matplotlib.pyplot as plt

yelp_csv = pd.read_csv('yelp_review.csv')

# DIMENSIONE DEL CSV RIGHE, COLONNE
dim_yelp_csv = yelp_csv.shape
print(dim_yelp_csv)

# ESTRAPOLARE IL DATAFRAME DEL CSV
print(pd.DataFrame(yelp_csv))

# Trova i valori nulli in un dataset
print(yelp_csv.isnull().sum())

# Esplorazione iniziale del dataset, descrizione della colonna business id. COUNT, UNIQUE, TOP E FREQ
print(yelp_csv['business_id'].describe())

# SCELGO IL TEXT PIU PRESENTE NEL DATASET
duplicate_text = yelp_csv['text'].describe()['top']

# VERIFICO TRAMITE TRUE/FALSE QUALE TESTO DELLA COLONNA TEXT E' UGUALE AL TESTO DUPLICATO. RITORNA UNA SERIES (COLONNA)
text_is_duplicated = yelp_csv['text'] == duplicate_text

# I PRIMI ELEMENTI DELLA SERIES
print(text_is_duplicated.head())

# COME TROVARE LA FREQUENZA, I VALORI FALSE E TRUE SONO SOMMABILI: TRUE = 1 E FALSE = 0
print(sum(text_is_duplicated))

# TROVO IL DATAFRAME INTERESSATO. LE COLONNE E LE RIGHE DOVE E' PRESENTE IL DUPLICATO
print(yelp_csv[text_is_duplicated])

stars = yelp_csv['stars'].value_counts()
stars.sort_values()
stars.plot.bar()
plt.show()