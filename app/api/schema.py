from pydantic import BaseModel
from typing import List, Dict, Optional, Union, Any

class Action(BaseModel):
    click: Optional[str] = None
    type: Optional[Dict[str,str]] = None
    select: Optional[Dict[str,str]] = None
    wait: Optional[Union[str,int]] = None

class CrawlRequest(BaseModel):
    url: Optional[str] = None
    actions: Optional[List[Action]] = []
    extract: Optional[Dict[str, str]] = {}

    # For site profile mode
    site_id: Optional[str] = None
    inputs: Optional[Dict[str, str]] = {}

class CrawlResponse(BaseModel):
    success: bool
    data: Dict[str, Any]
    error: Optional[str] = None
    site_id: Optional[str] = None
    inputs: Optional[Dict[str, str]] = {}
