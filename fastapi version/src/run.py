import uvicorn

from fastapp import app


if __name__ == "__main__":
    uvicorn.run(app)