from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"Texte":"Ceci est un text"}

@app.get('/listeEtudiant')
def liste():
    return [
        {"Cekah":"Licence en infomramatique"}, 
        {"Dominick":"Bacc + 5"}
        ]
    
if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)