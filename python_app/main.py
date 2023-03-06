from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    version = os.getenv('version', default = '0.0.1')
    instance_name = os.getenv('instance_name',default= 'OCI CI Host')
    return {"Message": f"With ❤️ from OCI Devops via OCI Container instance {instance_name}"}
