import json
qutesList=[]
quoteItem1={}
quoteItem1['questions']=""
quoteItem1['фты']=""
jsonString = json.dumps(qutesList, ensure_ascii=False)
jsonFile = open("data.json", "w", encoding="UTF-8")
jsonFile.write(jsonString)
jsonFile.close()