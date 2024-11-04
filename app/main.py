from fastapi import FastAPI, status, Depends,HTTPException
from sqlalchemy.orm import Session
from . import model
from .database import engine, get_db
from .schema import postcreate
from .model import Post
from .router import post, user, login,vote
model.Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins =['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(login.router)
app.include_router(vote.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/posts/{id}")
def update_post(id: int,updated_post:postcreate, db: Session = Depends(get_db)):
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return  post_query.first()
