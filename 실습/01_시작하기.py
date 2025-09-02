from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary="간단한 API", tags=["Simple"])#, description="매우 간단한 API임")
async def root():
    '''
    이것은 간단한 API임
    '''
    return {"message": "Hello World"}