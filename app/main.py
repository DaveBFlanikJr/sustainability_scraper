from fastapi import FastAPI
import uvicorn
from app.api.routes import router



app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "hello"}
app.include_router(router)

def main():
    uvicorn.run("app.main:app", host="127.0.0.1", port=3001, reload=True)

if __name__ == "__main__":
    main()
