import requests, time
from requests.structures import CaseInsensitiveDict
from typing import Union, Tuple, List
from .types import (
    StatusResponse,
    BaseResponse,
)

class GridApi:
    GRID_URL:str
    _headers:dict

    def __init__(self, url:str, secret:str=None) -> None:
        self.GRID_URL = url
        self._headers = {'X-REGISTRATION-SECRET': secret} if secret else CaseInsensitiveDict({'X-REGISTRATION-SECRET':''})

    def get_status(self) -> Union[StatusResponse, None]:
        response = requests.get(f'{self.GRID_URL}/status', headers=self._headers)
        if response.status_code == 200:
            response = response.json()
            return response.get('value', None)
        
    def get_queue(self) -> Tuple[int, List[dict]]:
        response = requests.get(f'{self.GRID_URL}/se/grid/newsessionqueue/queue', headers=self._headers)
        return response.status_code, response.json()['value']
        
    def clear_queue(self) -> Tuple[int, BaseResponse]:
        response = requests.delete(f'{self.GRID_URL}/se/grid/newsessionqueue/queue', headers=self._headers)
        time.sleep(1)
        return response.status_code, response.json()
    
    def delete_session(self, session_id:str=None) -> None:
        """
            If session_id is None, all sessions will be deleted
        """
        status = self.get_status()
        if status:
            for node in status['nodes']:
                for slot in node['slots']:
                    session = slot.get('session', None)
                    if session:

                        if session_id == session['sessionId'] or session_id is None:

                            node_uri = session.get('uri', None)
                            if not node_uri:
                                node_uri = node['uri']
                            requests.delete(f'{node_uri}/se/grid/node/session/{session_id}', headers=self._headers)
                            
                            if not session_id is None: return
                        
    def delete_sessions(self) -> None:
        self.delete_session()
                    
    def kill_all_sessions(self) -> None:
        self.delete_session()

    def count_sessions(self) -> int:
        count = 0
        status = self.get_status()
        if status:

            for node in status['nodes']:
                for slot in node['slots']:
                    if slot.get('session', False):
                        count += 1

        return count


