import requests
import re

def get_stock_ids():
    url = "http://old.tsetmc.com/tsev2/data/MarketWatchPlus.aspx"
    r = requests.get(url)
    ids = set(re.findall(r"\d{15,20}", r.text))
    return list(ids)

id_list = get_stock_ids()

def get_stock_detail():



    list_of_stock =[]
    for stock_id in id_list:
        url = f"https://old.tsetmc.com/Loader.aspx?ParTree=151311&i={stock_id}"
        r = requests.get(url)
        try:
            stock = {
                "code": stock_id,
            }
        except IndexError:
            return
        try:
            stock["name"] = re.findall(r"LVal18AFC='([\D]*)',", r.text)[0]
        except:
            continue
        list_of_stock.append(stock)
        print(list_of_stock)

    return list_of_stock
print(get_stock_detail())