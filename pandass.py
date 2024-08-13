import pandas as pd

dataset = {
    'car':123,
    'car2':456,
    'car3':567
}

df = pd.Series(dataset)
print(df)

data={
    'car':"bmw",
    'car1':"od",
    'car2':"mercides"
}

de=pd.read_csv('data.csv')
print(de)
aa=pd.options.display.max_rows
print(aa)
ss=pd.read_json('package.json')
print(ss)
