import pandas as pd

df = pd.read_csv('cleaned_total_stars.csv')
print(df.dtypes)

df["Mass"] =df["Mass"].apply(lambda x: x.replace('$', '').replace(',','')).astype('float')
df["Radius"] =df["Radius"].apply(lambda x: x.replace('$', '').replace(',','')).astype('float')

mass = df['Mass'].tolist()
radius = df['Radius'].tolist()


simass=[]
for data in mass:
    mul = data*1.989e+30
    simass.append(mul)

siradius=[]
for data in radius:
    mul2 = data*6.957e+8
    siradius.append(mul2)

gravity=[]
G = 6.674e-11
for index in range(0,len(mass)):
    g= (mass[index]*G)/((radius[index])**2)
    gravity.append(g)

df.to_csv("final.csv")