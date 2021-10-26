import pandas as pd
filename = "data_babyLaCuesta.csv"
df = pd.read_csv(filename) 
df_coin = df.loc[df['Relation'] != 'Non related']
print("\nTarget: saramambiche64")
print("Analizing friendships with:", filename[5:-4])
print("Coincidences:", df_coin.shape[0], "out of", df.shape[0], "\n")
print(df_coin)