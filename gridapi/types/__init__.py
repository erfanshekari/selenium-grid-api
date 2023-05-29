from typing import TypedDict, List, Any, Union

class BaseResponse(TypedDict):
    value: Any
    message: Union[str, None]

class SlotID:
    hostId: str
    id: str

Stereotype = TypedDict(
    "Stereotype",
    {
        "browserName": str,
        "browserVersion": str,
        "platformName": str,
        "se:noVncPort": int,
        "se:vncEnabled": bool,
    },
)

class Session(TypedDict):
    capabilities: dict
    sessionId: str
    start: str
    stereotype: Stereotype
    uri: str

class Slot(TypedDict):
    id: SlotID
    lastStarted: str
    session: Union[Session, None]
    stereotype: Stereotype

class Node(TypedDict):
    id: str
    uri: str
    maxSessions: int
    osInfo: dict
    heartbeatPeriod: int
    heartbeatPeriod: str
    version: str
    slots: List[Slot]

class StatusResponse(TypedDict):
    ready: bool
    nodes: List[Node]
    message: str
