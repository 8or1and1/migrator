import requests


class elmaConnector:
    def __init__(self, config, namespace, code):
        address = config['address']
        token = config['token']
        self.address = '{}/pub/v1/app/{}/{}/'.format(address, namespace, code)
        self.headers = {"Authorization": "Bearer {}".format(token)}
        self.column_names = self.get_column_names()

    def api_request(self, method, payload=None):
        if payload is None:
            payload = {}
        url = self.address + method
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def get_column_names(self):
        payload = {"size": 1}
        response = self.api_request('list', payload)
        column_names = [x for x in response.json()["result"]["result"][0].keys()]
        return column_names

    def create_element(id, name):
        pass
        # url = 'https://ddvowxahv2jug.elma365.ru/pub/v1/app/_system_catalogs/ContactStatus/create'
        # myobj = {'Context':{'__id':str(id), '__name':name}}
        # headers = {"Authorization": "Bearer e5e0da91-644e-43ac-aad9-3f39ff066cf4"}
        #
        # x = requests.post(url, json = myobj, headers=headers)
        # y = x.json()
        # return(y)
        return (1)
