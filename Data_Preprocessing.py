import pandas as pd


train = pd.read_csv('Big-Mart-Sales-III-master\Data\Train.csv') #檔案路徑

print('Item_Fat_Content的原始資料')
print(train['Item_Fat_Content'])
print('')

train.Item_Fat_Content.replace( ('Low Fat','Regular','low fat','LF', 'reg') , (1,0,1,1,0) ,inplace=True ) # Categorical Data

print('Item_Fat_Content處理後的資料')
print(train['Item_Fat_Content'])