import requests

def get_val_malum(val):
    url = f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    response = requests.get(url=url)

    if response.status_code != 200:
        return None
    
    data = response.json()

    for currency in data:
        if currency['Ccy'] == val:
            if val == 'USD':
                return f'<blockquote>{currency["CcyNm_UZ"]}</blockquote>\n\n1 USD 🇺🇸 = {currency["Rate"]} \nO\'zgarish 📈: {currency["Diff"]} \nSana📆: {currency["Date"]}'
            elif val == 'RUB':
                return f'<blockquote>{currency["CcyNm_UZ"]}</blockquote>\n\n1 RUB 🇷🇺 = {currency["Rate"]} \nO\'zgarish 📈: {currency["Diff"]} \nSana📆: {currency["Date"]}'
            elif val == 'EUR':
                return f'<blockquote>{currency["CcyNm_UZ"]}</blockquote>\n\n1 EUR 🇪🇺 = {currency["Rate"]} \nO\'zgarish 📈: {currency["Diff"]} \nSana📆: {currency["Date"]}'
            elif val == 'JPY':
                return f'<blockquote>{currency["CcyNm_UZ"]}</blockquote>\n\n1 JPY 🇯🇵 = {currency["Rate"]} \nO\'zgarish 📈: {currency["Diff"]} \nSana📆: {currency["Date"]}'
    else: 
        return "Bunday 🏳️ qiymat mavjud emas !"

