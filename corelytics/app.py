
import os

from fastapi import FastAPI, HTTPException

from models import FileModel, WSModel, SQLModel
from readers import WSReader, FileReader, SQLReader


path_files = os.getenv('path_files', '/var/dispatcher')
app = FastAPI()


@app.get('/')
async def healthcheck():
    return {"message": "Hello World"}


@app.post('/fileservice')
async def file_service(model: FileModel):
    if model.type_file not in ('csv', 'json', 'excel', 'parquet'):
        raise HTTPException(
            status_code=400,
            detail=f'type file "{model.type_file}" does not supported'
        )

    path_file = f'{path_files}/{model.type_file}/{model.filename}'
    exists = os.path.isfile(path_file)

    if exists is False:
        raise HTTPException(
            status_code=404,
            detail=f'file {model.filename} does not exists'
        )

    file_process = FileReader(model.gid, path_file, model.separator)
    file_process.main()

    return {'message': 'success'}


@app.post('/wsservice')
async def ws_service(model: WSModel):

    return {'message': 'in ws service'}


@app.post('/sqlservice')
async def sql_service(model: SQLModel):

    return {'message': 'in sql service'}
