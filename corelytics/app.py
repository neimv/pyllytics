
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
    model.status_code = 200 if model.status_code is None \
        else model.status_code

    ws_process = WSReader(model.gid, model.url, model.status_code)
    ws_process.main()

    return {'message': 'success'}


@app.post('/sqlservice')
async def sql_service(model: SQLModel):
    possible_drivers = {
        'mysql': 3306,
        'maria': 3306,
        'postgres': 5432
    }
    drivers = ', '.join(possible_drivers.keys())

    if model.driver not in possible_drivers.keys():
        raise HTTPException(
            status_code=400,
            detail=(
                f'db driver "{model.driver}" does not supported'
                f', supported db driver are {drivers}'
            )
        )

    model.port = model.port if model.port is not None \
        else possible_drivers[model.driver]

    sql_process = SQLReader(
        model.gid, model.user, model.password, model.db, model.host,
        model.port, model.driver, model.resource, model.type_read
    )
    sql_process.main()

    return {'message': 'success'}
