from fastapi import FastAPI
import uvicorn
import mysql.connector as myconnect

app = FastAPI()
#--------------------------------------------------------------------------
def sendJson(reponses, nomColonne):
    resultats = [] 
    
    for reponse in reponses:
        resultat = {}
        for ligne, donnee in zip(nomColonne, reponse):
            resultat[ligne] = donnee
        resultats.append(resultat)
    return resultats
#--------------------------------------------------------------------------
@app.get('/')
def lieux():
    try:
        conn = myconnect.connect(host='localhost',database='area',user='root',password='')
        cursor = conn.cursor()

        req = "SELECT * FROM lieux"
        cursor.execute(req)

        listeLieux = cursor.fetchall()
        lieuxs ={}
        for lieux in listeLieux:
            lieuxs[lieux[0]]=lieux[1]
        nomColonne = [
            'id', 
            'Lieux', 
            ]

    except myconnect.error as error:
        print(error)
    return sendJson(lieuxs, nomColonne)
    

    
if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)