import pandas as pd

df=pd.read_excel("pd_14a.xlsx")
print("\nNew DataFrames:")
print(df)
df1=pd.read_excel("pd_14b.xlsx")
print(df1)


print('\n"one_to_one”: check if merge keys are unique in both left and right datasets:"')
#df_one_to_one = pd.merge(df, df1, validate = "one_to_one")
#print(df_one_to_one)
#df_one_to_one.to_excel("pd_14_res.xlsx")

print('\n"one_to_many” or “1:m”: check if merge keys are unique in left dataset:')
df_one_to_many = pd.merge(df, df1, validate = "one_to_many")
print(df_one_to_many)
print('“many_to_one” or “m:1”: check if merge keys are unique in right dataset:')
df_many_to_one = pd.merge(df, df1, validate = "many_to_one")
print(df_many_to_one)

# Erklären sie was diese Programm macht?