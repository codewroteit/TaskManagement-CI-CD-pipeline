from fastapi import FastAPI
#FastAPI to allow python to use FastAPI framework

app = FastAPI()  # creating of FastAPI application, the variable app will represent the web application

@app.get("/")
def home();
    return {"message": "Devops Status App is running" }

@app.get("/health")
def health();
    return {"status": "Healthy" }

@app.get("/version")
def version();
    return {"version": "1.0.0"}
