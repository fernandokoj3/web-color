import socket
from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime, timezone

router = APIRouter(
    tags=["Home"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return templates.TemplateResponse(
        "index-yellow.html",
        {
            "request": request,
            "hostname": hostname,
            "ip_address": ip_address,
            "app_name": "web-color",
            "env": "local",
            "now": datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z"),
        }
    )