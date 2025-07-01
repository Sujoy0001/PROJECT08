from pydantic import BaseModel
from typing import Literal

class reviews(BaseModel):
    
    user_review : str
    user_ratting: Literal[
        "1","2","3","4","5"
    ]