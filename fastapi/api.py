from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
import os


app: FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/generation/{generation}/img/{img}")
async def search_img(generation: int, img: int):
    current: Path = Path()
    img_name = str(img) + ".svg"
    url_path: str = "data/" + str(generation) + "/" + img_name
    file_path: Path = current/url_path
    return FileResponse(path=file_path, media_type="image/svg+xml")

@app.get("/archive")
async def archive():
    root: str = os.getcwd()
    archive_dir = root + "\\archive"
    archive_dirs = [_ for _ in os.listdir(archive_dir) if os.path.isdir(os.path.join(archive_dir, _))]
    result_list = []
    for archive_dir in archive_dirs:
        each_archive_dir = root + "\\archive\\" + archive_dir + "\\"
        generation_dirs = [_ for _ in os.listdir(each_archive_dir) if os.path.isdir(os.path.join(each_archive_dir, _))]
        result_list.append({archive_dir: generation_dirs})
    return {"archive": result_list}

@app.get("/archive/{dir_name}/generation/{generation}/img/{img}")
async def search_archive_img(dir_name: str, generation: int, img: int):
    current: Path = Path()
    img_name = str(img) + ".svg"
    url_path: str = "archive/" + dir_name + "/" + str(generation) + "/" + img_name
    file_path: Path = current/url_path
    return FileResponse(path=file_path, media_type="image/svg+xml")