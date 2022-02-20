from fastapi import FastAPI
import uvicorn
import mysql.connector as myconnect

app = FastAPI()

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

    except myconnect.error as error:
        print(error)
    
    return lieuxs

# print(lieux())
#    return listeLieux[lieux[0]:lieux[1]]
# @app.get('/')
# def index():
#     return {"Texte":"Ceci est un text"}

# @app.get('/listeEtudiant')
# def liste():
#     return [
#         {"Cekah":"Licence en infomramatique"}, 
#         {"Dominick":"Bacc + 5"}
#         ]
    
if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)