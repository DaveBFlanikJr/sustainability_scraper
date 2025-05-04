from pydantic import BaseModel
from typing import List, Dict, Optional, Union, Any

class Action(BaseModel):
    click: Optional[str] = None
    type: Optional[Dict[str,str]] = None
    select: Optional[Dict[str,str]] = None
    wait: Optional[Union[str,int]] = None

class CrawlRequest(BaseModel):
    url: str
    actions: List[Action]
    extract: Dict[str,str]

class CrawlResponse(BaseModel):
    success: bool
    data: Dict[str, Any]
    error: Optional[str] = None
