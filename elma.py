import requests
def get_elma_column_names():
    url = 'https://ddvowxahv2jug.elma365.ru/pub/v1/app/_system_catalogs/ContactStatus/list'
    myobj = {}
    headers = {"Authorization": "Bearer e5e0da91-644e-43ac-aad9-3f39ff066cf4"}

    x = requests.post(url, json = myobj, headers=headers)
    y = x.json()["result"]["result"][0].keys()
    return(y)
def create_element(id, name):
    url = 'https://ddvowxahv2jug.elma365.ru/pub/v1/app/_system_catalogs/ContactStatus/create'
    myobj = {'Context':{'__id':str(id), '__name':name}}
    headers = {"Authorization": "Bearer e5e0da91-644e-43ac-aad9-3f39ff066cf4"}

    x = requests.post(url, json = myobj, headers=headers)
    y = x.json()
    return(y)