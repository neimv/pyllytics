
from app import app


@app.get('/fileservice')
async def file_service():

    return {'message': 'in file service'}


@app.get('/wsservice')
async def ws_service():

    return {'message': 'in ws service'}


@app.get('/sqlservice')
async def sql_service():

    return {'message': 'in sql service'}
