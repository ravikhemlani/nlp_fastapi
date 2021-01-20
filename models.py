from sqlalchemy import Column, Integer, String
from database import Base


# model that represents the table in our database
class Item(Base):
    __tablename__ = "entity_data"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    entity = Column(String)
    text = Column(String)