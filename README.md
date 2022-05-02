![](thumb_250x64.jpg)
Курс
# Продвинутый Python
## Портфолио по анализу данных
---
## Часть 1 Анализ данных.   numpy и pandas
###  Задание: импорт данных

Возьмите данные по вызовам пожарных служб в Москве за 2015-2019 годы:
https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv
Получите из них фрейм данных (таблицу значений). По этому фрейму вычислите среднее значение вызовов пожарных машин в месяц в одном округе Москвы, округлив до целых
_Примечание: найдите среднее значение вызовов, без учета года_

     Решение:    
>import pandas as pd
data = pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter=";")
print (data["Calls"].mean().round())


>493.0
--- 

## Часть 1 Анализ данных.   Индексы и объединение фреймов
###  Задание: данные из нескольких источников
Получите данные по безработице в Москве:
https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv
Объедините эти данные индексами (Месяц/Год) с данными из предыдущего задания (вызовы пожарных) для Центральный административный округ:
https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv
Найдите значение поля UnemployedMen в том месяце, когда было меньше всего вызовов в Центральном административном округе.

    Решение:    
>import pandas as pd
data1 = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
data1 = data1.set_index(["Year", "Period"])
data2 = pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter=";")
data2 = data2.set_index(["AdmArea", "Year", "Month"])
data2 = data2.loc["Центральный административный округ"]
data2.index.names = ["Year", "Period"]
data = pd.merge(data1, data2, left_index=True, right_index=True)
data = data.reset_index()
data = data.set_index("Calls")
data = data.sort_index()
print (data["UnemployedMen"][0:1])


>Calls
220    13465
Name: UnemployedMen, dtype: int64
--- 
## Часть 1 Анализ данных.   Линейная регрессия
## Задание: предсказание на 2020 год
Возьмите данные по безработице в городе Москва:
video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv
Сгруппируйте данные по годам, и, если в году меньше 6 значений, отбросьте эти годы.
Постройте модель линейной регрессии по годам среднего значения отношения UnemployedDisabled к UnemployedTotal (процента людей с ограниченными возможностями) за месяц и ответьте, какое ожидается значение процента безработных инвалидов в 2020 году при сохранении текущей политики города Москвы?
Ответ округлите до сотых. Например, 2,32

  Решение:    
>import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
data["UDP"] = 100*data["UnemployedDisabled"]/data["UnemployedTotal"]
data_group = data.groupby("Year").filter(lambda x: x["UDP"].count() > 5)
data_group = data_group.groupby("Year").mean()
x = np.array(data_group.index).reshape(len(data_group.index), 1)
y = np.array(data_group["UDP"]).reshape(len(data_group.index), 1)
model = LinearRegression()
model.fit(x, y)
print (np.round(model.predict(np.array(2020).reshape(1, 1)), 2))


>[[1.52]]
---
## Часть 1 Анализ данных.   Фильтрация и изменение данных
## Задание: выделение данных
Получите данные по безработице в Москве:
https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv
Найдите, с какого года процент людей с ограниченными возможностями (UnemployedDisabled) среди всех безработных (UnemployedTotal) стал меньше 2%.

    Решение:    
>import pandas as pd
data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
data["Sum"] = data.apply(lambda x: 100*x[6]/x[7], axis=1)
data = data[data["Sum"] < 2]
data = data.set_index("Year")
data = data.sort_index()
print (data.index[0:1])
>Int64Index([2018], dtype='int64', name='Year')
---
## Часть 2 Импорт и парсинг данных
## 2.1 Импорт данных
Задание: получение данных по API
Изучите API Геокодера Яндекса
tech.yandex.ru/maps/geocoder/doc/desc/concepts/input_params-docpage/
и получите ключ API для него в кабинете разработчика.
Выполните запрос к API и узнайте долготу точки на карте (Point) для города Самара.
Внимание: активация ключа Геокодера Яндекса может занимать несколько часов (до суток).
В качестве запасного варианта можно использовать этот ключ - 3f355b88-81e9-4bbf-a0a4-eb687fdea256 - он только для выполнения этого задания!

   Решение:    
>import requests
import pandas as pd
import json
r = requests.get("https://geocode-maps.yandex.ru/1.x?geocode=Самара&apikey=3f355b88-81e9-4bbf-a0a4-eb687fdea256&format=json&results=1")
geo = json.loads(r.content)
#print(geo)
print(geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(" ")[0])


>{'response': {'GeoObjectCollection': {'metaDataProperty': {'GeocoderResponseMetaData': {'request': 'Самара', 'results': '1', 'found': '1'}}, 'featureMember': [{'GeoObject': {'metaDataProperty': {'GeocoderMetaData': {'precision': 'other', 'text': 'Россия, Самара', 'kind': 'locality', 'Address': {'country_code': 'RU', 'formatted': 'Россия, Самара', 'Components': [{'kind': 'country', 'name': 'Россия'}, {'kind': 'province', 'name': 'Приволжский федеральный округ'}, {'kind': 'province', 'name': 'Самарская область'}, {'kind': 'area', 'name': 'городской округ Самара'}, {'kind': 'locality', 'name': 'Самара'}]}, 'AddressDetails': {'Country': {'AddressLine': 'Россия, Самара', 'CountryNameCode': 'RU', 'CountryName': 'Россия', 'AdministrativeArea': {'AdministrativeAreaName': 'Самарская область', 'SubAdministrativeArea': {'SubAdministrativeAreaName': 'городской округ Самара', 'Locality': {'LocalityName': 'Самара'}}}}}}}, 'name': 'Самара', 'description': 'Россия', 'boundedBy': {'Envelope': {'lowerCorner': '49.732198 53.091785', 'upperCorner': '50.390439 53.551185'}}, 'Point': {'pos': '50.100202 53.195878'}}}]}}}

>50.100202
---

## Часть 2 Импорт и парсинг данных
## Задание: 2.2 Парсинг данных, получение котировок акций
Получите данные по котировкам акций со страницы:
mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019
и найдите, по какому тикеру был максимальный рост числа сделок (в процентах) за 1 ноября 2019 года.


   Решение:    
>import requests
import pandas as pd
from bs4 import BeautifulSoup
r = requests.get("https://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019")
html = BeautifulSoup(r.content)
table = html.find('table', {'id':'marketDataList'})
rows = []
trs = table.find_all('tr')
for tr in trs:
    tr = [td.get_text(strip=True) for td in tr.find_all('td')]
    if len(tr) > 0:
        rows.append(tr)
data = pd.DataFrame(rows, columns=["Тикер", "Дата", "Сделки", "C/рост", "С/%", "Закрытие", "Открытие", "min", "max", "avg", "шт", "руб", "Всего"])
data = data[data["Сделки"] != "N/A"]
data["С/%"] = data["С/%"].str.replace("−","-").str.replace("%","").astype(float)
data = data.set_index("С/%")
data = data.sort_index(ascending=False)
print (data["Тикер"].head(1))

>С/%
11.0    ИКРУСС-ИНВ
Name: Тикер, dtype: object
---
## Часть 2 Импорт и парсинг данных
## 2.3 Веб-скрепинг
## Задание: парсинг интернет-магазина
Используя парсинг данных с маркетплейса beru.ru, найдите, на сколько литров отличается общий объем холодильников Саратов 263 и Саратов 452?
Для парсинга можно использовать зеркало страницы beru.ru с результатами для холодильников Саратов по адресу:
video.ittensive.com/data/018-python-advanced/beru.ru/

   Решение:    
>im
>import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.0.358 Yowser/2.5 Safari/537.36"}
r = requests.get("https://beru.ru/search?cvredirect=2&suggest_reqId=27865074762321487883702093457804&text=%D1%81%D0%B0%D1%80%D0%B0%D1%82%D0%BE%D0%B2", headers=headers)
html = BeautifulSoup(r.content)
print (r.content)
links = html.find_all("a", {"class": "grid-snippet__react-link"})
link_263 = ''
link_452 = ''
for link in links:
    if str(link).find("Саратов 263") > -1:
        link_263 = link["href"]
    if str(link).find("Саратов 452") > -1:
        link_452 = link["href"]
>
>def find_volume (link):
    r = requests.get("https://beru.ru" + link)
    html = BeautifulSoup(r.content)
    volume = html.find_all("span", {"class": "_112Tad-7AP"})
    return int(''.join(i for i in volume[2].get_text() if i.isdigit()))
>
>if link_263 and link_452:
    volume_263 = find_volume(link_263)
    volume_452 = find_volume(link_452)
    diff = max(volume_263, volume_452) - min(volume_263, volume_452)
    print (diff)

    >