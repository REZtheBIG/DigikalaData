import json
import requests
import pandas as pd
from datetime import date

DB = []
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
Base_url = "https://api.digikala.com/v1/product/2952640/"

# price NA 117348
# Price A  7512762

URL = requests.get(Base_url.format(id), headers=headers)
text = URL.text
data = json.loads(text)
prettyJSON = json.dumps(data, indent=4, ensure_ascii=False)
print(prettyJSON)
with open('Product_json_data.json', 'w', encoding='utf8') as outfile:
    outfile.write(prettyJSON)

Product_Name = data['data']['product']['title_fa']
Product_ID = data['data']['product']['id']
Brand = data['data']['product']['data_layer']['brand']
Group = data['data']['product']['data_layer']['item_category2']
Availability = str(data['data']['seo']['open_graph']['availability'])
# Price = ((data['data']['product']['default_variant']['price']['selling_price']) / 10)
Main_Category = data['data']['product']['data_layer']['item_category3']
Sub_Category = data['data']['product']['data_layer']['item_category4']
if 'price' in data['data']['product']['default_variant']:
    Price = (int(data['data']['product']['default_variant']['price']['selling_price']) / 10)
else:
    Price = "Product not available"
# Price = (int(data['data']['product']['default_variant']['price']['selling_price']) / 10)
Date = date.today()
Product_info = {'ProductName': Product_Name,
                'ProductID': Product_ID,
                'Brand': Brand,
                'ِDataGroup': Group,
                'MainCategory': Main_Category,
                'Sub'
                'Category': Sub_Category,
                'Price': Price,
                'Date': Date,
                'Availability': Availability}
DB.append(Product_info)
print(" Product_Name = " + data['data']['product']['title_fa'] + "\n",
      "Product_ID = " + str(data['data']['product']['id']) + "\n",
      "Brand = " + data['data']['product']['data_layer']['brand'] + "\n",
      "Group = " + str(data['data']['product']['data_layer']['item_category2']) + "\n",
      "Main_Category = " + str(data['data']['product']['data_layer']['item_category3']) + "\n",
      "Sub_Category = " + str(data['data']['product']['data_layer']['item_category4']) + "\n",
      "Price = " + str(Price) + "\n",
      )
print(Availability)
print(Product_info)
df = pd.DataFrame(DB)
df.to_csv('DB.csv', encoding='utf-8')
print(df)
