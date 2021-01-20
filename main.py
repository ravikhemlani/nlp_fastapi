from web_scraper import get_text, get_entities, get_entity_text
from fastapi import FastAPI, Request, Depends, File, UploadFile, BackgroundTasks
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import collections

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


# get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home():
    return "Welcome to our NLP Service API!"


@app.get("/url/content")
async def get_url_text(url: str = None):

    url_text = get_text(url)
    return {'url_text': url_text}


@app.get("/url/entities")
async def get_url_entities(url: str = None):

    article_text = get_text(url)
    entities = set(get_entities(article_text))
    return {'Entities': entities}


@app.get("/url/entity-text")
async def get_url_entity_text(url: str = None, entity: str = None):
    article_text = get_text(url)
    texts = get_entity_text(article_text, entity.upper())
    items = collections.Counter(str(item) for item in texts)
    return {f"Text for '{entity}' ": items}


@app.post("/add/")
async def add_urldata(url: str = None, db: Session = Depends(get_db)):
    try:
        for entity in set(get_entities(get_text(url))):
            item = models.Item()
            item.url = url
            item.entity = entity
            item.text = str(get_entity_text(get_text(item.url), entity))
            db.add(item)
        db.commit()
    finally:
        db.close()
    return {"message": "Successfully added data into the database"}


@app.get("/database")
async def view_database(db: Session = Depends(get_db)):
    rows = db.query(models.Item).all()
    return rows


@app.get("/database/entities")
async def extract_entities(url: str, db: Session = Depends(get_db)):
    rows = db.query(models.Item).filter(models.Item.url == url).all()
    return rows


@app.get("/database/entity-texts")
async def extract_entity_text(url: str, entity: str, db: Session = Depends(get_db)):
    rows = db.query(models.Item).filter(models.Item.url == url, models.Item.entity == entity.upper()).all()
    return rows


@app.post("/upload/")
async def add_data_from_file(file: UploadFile = File(...)):
    """
    Future implementation, users can have the option of either uploading a file entering a URL
    """
    return {"filename": file.filename}