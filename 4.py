import requests

r = requests.get('http://52.233.158.172/change/api/hr/team/confirm?id=4&repository=https://gitlab.com/thearena91/king-init', headers = {'X-Authorization' : 'THVjcmVodWxrOjo='})

r.text