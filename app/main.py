from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from fastapi import FastAPI, Request, HTTPException, Depends, Cookie
import json
from auth import py_jwt
from order import job_order, sample_order
from sidebar import py_sidebar
from login import py_login
from filter import py_filter

auth_scheme = py_jwt.JWTBearer()

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "success"}


@app.post("/OrderEntry/login")
async def login(request: Request):
    try:
        request = await request.json()
        print(request,"111")
        response = py_login.fn_login(request)
        return response
    except Exception as e:
        print(str(e))

@app.get("/OrderEntry/get_sidebar")
async def get_sidebar(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_sidebar.main_menu(decoded)
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")

# <------------------------------------- Dropdown Api Starts ---------------------------------------------------------->

@app.get("/OrderEntry/get_order_type")
async def get_order_type(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.orderType()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")


@app.get("/OrderEntry/get_pinning_percent")
async def get_pinning_percent(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.PinningPercent()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")


@app.get("/OrderEntry/get_packing_type")
async def get_packing_type(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.PackingType()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")


@app.get("/OrderEntry/get_count_type")
async def get_count_type(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.CountType()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")


@app.get("/OrderEntry/get_loom_type")
async def get_loom_type(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.LoomType()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")


@app.get("/OrderEntry/get_payment_terms")
async def get_payment_terms(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.PaymentTerms()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")


@app.get("/OrderEntry/get_purchase_mode")
async def get_purchase_mode(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.PurchaseMode()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")

@app.get("/OrderEntry/get_transport_mode")
async def get_transport_mode(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.TransportMode()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")

@app.get("/OrderEntry/get_freight_rate")
async def get_freight_rate(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.FreightRate()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")

@app.get("/OrderEntry/get_fabric_type")
async def get_fabric_type(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_filter.FabricType()
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")



# <------------------------------------- Dropdown Api Ends ------------------------------------------------------------>

@app.post("/OrderEntry/insert_job_order_entry")
async def insert_job_order_entry(request: Request, decoded=Depends(auth_scheme)):
    if decoded:
        try:
            request = await request.json()
            response = job_order.insert_job_order(request, decoded)
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")

@app.post("/OrderEntry/insert_sample_order_entry")
async def insert_sample_order_entry(request: Request, decoded=Depends(auth_scheme)):
    if decoded:
        try:
            request = await request.json()
            response = sample_order.insert_sample_order(request, decoded)
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=811)
