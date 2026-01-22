from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
from data_handler import csv_to_df, categorization_by_range_of_injury, handling_missing_values
from db import init_db

app = FastAPI()

@app.post("/upload")
def upload_csv_and_save_to_db(file: UploadFile = File(...)):
    try:
        init_db()

        if file.content_type != 'text/csv':
            raise HTTPException(status_code=422, detail='pleas try again with csv file')
        data = file.file
        df = csv_to_df(data)
        categorization_by_range_of_injury(df)
        handling_missing_values(df)
        
        return {"status": "success",
                "inserted_records": len(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="an error")


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)