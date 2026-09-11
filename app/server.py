from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel, EmailStr
from rag.retrieval import get_answer
from conf.utility import set_data, get_data

app = FastAPI()


class Employee(BaseModel):
    emp_id: int
    name: str
    mobile_number: str
    email: EmailStr
    role: str


class EmployeeResponse(BaseModel):
    name: str


API_KEY = "my-application"


def verify_api_key(requests: Request):
    api_key = requests.headers.get("x-api-key")

    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized Access")

    return True


def log_request(function):
    def wrapper():
        print("Started Request")
        result = function()
        print("Request Completed")
        return result

    return wrapper


@app.get("/")
@log_request
def temp_function():
    return "Server is running"


@app.post("/send-message")
def send_message(user_message: str):
    result = get_answer(user_query=user_message)
    return result


@app.post("/employee", status_code=201, response_model=EmployeeResponse)
def create_employee(payload: Employee, api_key: bool = Depends(verify_api_key)):
    try:

        result = set_data(
            emp_id=payload.emp_id,
            name=payload.name,
            email=payload.email,
            mobile_number=payload.mobile_number,
            role=payload.role,
        )

        return {"name": payload.name, "email": payload.email}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Serevr Error : {e}")
