"""
FastAPI app called 'Bookipedia' that serves information about books and their authors. A simple example of a
"many-to-many" relationship *with* extra data. This solution uses SQLAlchemy Association Proxies
"""
from fastapi import FastAPI
from .routes.index import pfc
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="PFC")

app.include_router(pfc)


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "127.0.0.1:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

