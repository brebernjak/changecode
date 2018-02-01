import requests

r = requests.get('http://52.233.158.172/change/api/hr/team/confirm?id=4&repository=https://github.com/brebernjak/changecode', headers = {'X-Authorization' : 'THVjcmVodWxrOjo='})

r.text