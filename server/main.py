from fastapi import FastAPI
from pydantic import BaseModel
from time import strftime

app = FastAPI()

class CpuUsageBody(BaseModel):
    cpu_usage: float


@app.post("/cpu-monitor")
def cpu_monitor(body: CpuUsageBody) -> None:
    print(f"[{strftime('%H:%M:%S')}] cpu_usage: {body.cpu_usage}")
    return None 

