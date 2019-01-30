import requests

def række_ting(række):
    række = række.replace('\n', '')
    felter = række.split('</td>')  
    z = felter[0][8:]
    symbol = felter[1][4:]

    navn = felter[2]
    link_start = navn.find('<a href=')
    link_slut = navn.find('"', link_start+10)
    link = navn[link_start+9:link_slut]
    link = 'https://da.wikipedia.org'+link
    seneste_komma = navn.find(',')
    while seneste_komma > -1:
        navn = navn[seneste_komma+1:]
        seneste_komma = navn.find(',')
    navn = navn.replace('(*)', '')
    navn = navn.replace('(**)', '')
    navn = navn.replace('(¤)', '')
    navn = navn.strip()
    
    titel_start = navn.find('">')
    titel_slut = navn.find('</a>')
    if titel_slut > -1:
        navn = navn[titel_start+2:titel_slut]
    return z, symbol, navn, link

response = requests.get('https://da.wikipedia.org/wiki/Grundstoffer_efter_atomnummer')
fullpage = response.text
tabelstart = fullpage.find('<table')
tabelslut = fullpage.find('</table')
tabel = fullpage[tabelstart:tabelslut]
tabelslut = tabel.rfind('<td ') 
tabel = tabel[:tabelslut-6]
rækker = tabel.split('</tr>')

del rækker[-1]
del rækker[0]
for række in rækker:
    print (række_ting(række))
