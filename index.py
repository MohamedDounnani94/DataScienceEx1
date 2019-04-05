import numpy
import pandas as pd
import matplotlib.pyplot as plt

# yelp_csv = pd.read_csv('yelp_review.csv')

# DIMENSIONE DEL CSV RIGHE, COLONNE
# dim_yelp_csv = yelp_csv.shape
# print(dim_yelp_csv)

# ESTRAPOLARE IL DATAFRAME DEL CSV
# print(pd.DataFrame(yelp_csv))

# Trova i valori nulli in un dataset
# print(yelp_csv.isnull().sum())

# Esplorazione iniziale del dataset, descrizione della colonna business id. COUNT, UNIQUE, TOP E FREQ
# print(yelp_csv['business_id'].describe())

# SCELGO IL TEXT PIU PRESENTE NEL DATASET
# duplicate_text = yelp_csv['text'].describe()['top']

# VERIFICO TRAMITE TRUE/FALSE QUALE TESTO DELLA COLONNA TEXT E' UGUALE AL TESTO DUPLICATO. RITORNA UNA SERIES (COLONNA)
# text_is_duplicated = yelp_csv['text'] == duplicate_text

# I PRIMI ELEMENTI DELLA SERIES
# print(text_is_duplicated.head())

# COME TROVARE LA FREQUENZA, I VALORI FALSE E TRUE SONO SOMMABILI: TRUE = 1 E FALSE = 0
# print(sum(text_is_duplicated))

# TROVO IL DATAFRAME INTERESSATO. LE COLONNE E LE RIGHE DOVE E' PRESENTE IL DUPLICATO
# print(yelp_csv[text_is_duplicated])

# stars = yelp_csv['stars'].value_counts()
# stars.sort_values()
# stars.plot.bar()
# plt.show()

# import csv
amazon_csv = pd.read_csv('bestselleramazon.csv')

#print(amazon_csv['Produttore'].describe())

# i brand piu numerosi
"""brands = amazon_csv['produttore'].value_counts()
brands.sort_values()
brands.plot.bar()
plt.show()"""

# la versione piu frequente
api = amazon_csv['api']
count_api = api.value_counts()
count_api.sort_values()
# count_api.plot.bar()
# plt.show()

# aspect ratio piu frequente
aspect_ratio = amazon_csv['aspect_ratio']
count_aspect_ratio = aspect_ratio.value_counts()
print(count_aspect_ratio)
# plt.show()

# aspect ratio dei cellulari top 10
top_phones = amazon_csv.head(10)
top_phones_aspect_ratio = top_phones['aspect_ratio']
count_top_phones = top_phones_aspect_ratio.value_counts()
print(count_top_phones)
# count_top_phones.sort_values()
# count_top_phones.plot.bar()
# plt.show()

# versione dei cellulari top 10
top_phones_version = top_phones['versionwe']
count_top_phones_version = top_phones_version.value_counts()
print(count_top_phones_version)
# count_top_phones_version.sort_values()
# count_top_phones_version.plot.bar()
# plt.show()

# produttori dei cellulari top 10
top_phones_mark = top_phones['produttore']
count_top_phones_mark = top_phones_mark.value_counts()
count_top_phones_mark.sort_values()
count_top_phones_mark.plot.bar()
plt.show()
"""amazon_csv.plot(figsize=(20,5))
names = amazon_csv['Nome']
reviews = amazon_csv['Recensioni']
plt.rcParams.update({'font.size': 6})
plt.bar(names, reviews)
plt.show()"""
