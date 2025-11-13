from fastapi import FastAPI


app = FastAPI()


@app.get('/article')
async def get_article():
    return "Cool article"


