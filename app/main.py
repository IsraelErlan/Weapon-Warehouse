from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
from data_handler import csv_to_df
from db import create_weapon_arehouse_table

app = FastAPI()

@app.post("/upload")
def upload_csv_and_save_to_db(file: UploadFile = File(...)):
    create_weapon_arehouse_table()

    if file.content_type != 'text/csv':
        raise HTTPException(status_code=422, detail='pleas try again with csv file')
    data = file.file
    df = csv_to_df(data)
    
    return {"filename": len(df)}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)