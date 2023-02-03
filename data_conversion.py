import pandas as pd

df = pd.read_csv('final_data.csv')
print(df.dtypes)

df["Radius"] =df["Radius"].apply(lambda x: x.replace('$', '').replace(',','')).astype('float')

mass = df['Mass'].tolist()
radius = df['Radius'].tolist()


df["Mass"] =df["Mass"]*1.989e+30
df["Radius"] =df["Radius"]*6.957e+8

gravity=[]
G = 6.674e-11
for index in range(0,len(mass)):
    g= (mass[index]*G)/((radius[index])**2)
    gravity.append(g)
df["Gravity"]=gravity

df.to_csv("final.csv")
