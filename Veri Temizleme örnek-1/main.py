import pandas as pd

veri = pd.DataFrame({"a":["bir","iki"]*3,"b":[1,1,2,3,2,3]})
print(veri)
print()

#duplicated komutu satırın tekrar edip etmediğini kontrol eder
print(veri.duplicated())
print()

#drop_duplicated komutu tekrar eden satıri kaldırır.
print(veri.drop_duplicates())
print()

veri["c"] =range(6)
print(veri)
print()

print(veri.drop_duplicates("a"))