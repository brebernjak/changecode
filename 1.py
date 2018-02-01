import requests

r = requests.post('http://52.233.158.172/change/api/hr/account/register', data = {
  "Teamname": "Lucrehulk",
  "Password": "tosipjomic",
  "Members": [
    {"name" : "Bartol",
      "surname" : "Rebernjak",
      "mail" : "bartol.rebernjak@fer.hr"
    },
    {"name" : "Josip",
      "surname" : "Tomić",
      "mail" : "josip.tomic@fer.hr"
    },
    {"name" : "Luka",
      "surname" : "Matejić",
      "mail" : "lmatejic@tvz.hr"
    },
    {"name" : "Luka",
      "surname" : "Kovačić",
      "mail" : "luka.kovacic2@fer.hr"
    }
    ]
}, headers = {'content-type': 'application/json'})

r.text