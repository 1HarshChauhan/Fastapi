from sqlalchemy import Column,Integer,String,Boolean
from database import Base

class Todo(Base):
    __tablename__ ="Todo"
    
    Id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True,nullable=False)
    descriptions=Column(String)
    done=Column(Boolean,default=False)
    