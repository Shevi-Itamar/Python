from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import zipfile
from typing import Dict
from Alert import Alert
from Graph import Graph

app = FastAPI()


@app.post("/alert")
async def alert_analysis(file: UploadFile = File(...)):
    try:
        with zipfile.ZipFile(file.file) as z:
            results = {}
            for file_info in z.infolist():
                if file_info.filename.endswith('.py'):
                    with z.open(file_info) as f:
                        alert = Alert(f)
                        results[file_info.filename] = alert.get_alerts()
        return results

    except zipfile.BadZipFile:
        return JSONResponse(status_code=400, content={"error": "Invalid ZIP file"})


@app.post("/analyze")
def graph_analyze(file: UploadFile = File(...)):
    graph = Graph(file)
    return graph.get_graph_image()