import requests

r = requests.get('http://52.233.158.172/change/api/hr/team/details/4', data = {
  "Teamname": "Lucrehulk",
  "Password": "tosipjomic"
}, headers = {'X-Authorization' : 'THVjcmVodWxrOjo='})

r.text