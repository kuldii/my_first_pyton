# Need to install first (if some packages have not been installed previously)
# >> python3 -m pip install beautifulsoup4
# or
# >> pip install beautifulsoup4
# 
# >> python3 -m pip install requests
# or
# >> pip install requests

from bs4 import BeautifulSoup
import requests

try:
    fileName = "text_6_var_12"
    urlAPI = "http://numbersapi.com/random/trivia?json"
    responseAPI = requests.get(urlAPI)
    dataJson = responseAPI.json()
    
    with open("assets/result/6/"+fileName+"_result.html", 'w', encoding='utf-8') as fileHtml:
        htmlContent='''<html>
        <body>
            <div id="data">
            </div>
        </body>
        </html>'''
        
        beautifulSoup = BeautifulSoup(htmlContent, "html.parser")
        divData = beautifulSoup.select_one("#data")
        
        dataH1 = '<h1>Number Trivia</h1>'
        divData.append(BeautifulSoup(dataH1, 'html.parser'))
        
        dataNumber = '<p><b>Number : '+ str(dataJson["number"]) +'</b></p>'
        divData.append(BeautifulSoup(dataNumber, 'html.parser'))
        dataText = '<i>Trivia : '+ str(dataJson["text"]) +'</i>'
        divData.append(BeautifulSoup(dataText, 'html.parser'))
        
        fileHtml.write(str(beautifulSoup.prettify()))
        
except Exception as e:
    print(e)