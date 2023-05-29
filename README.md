# Selenium Grid Python API

Features
* Grid status (GET)
* Queue Actions (GET, DELETE)
* Terminate Sessions using sessionId (DELELTE)

### How to use
~~~python
from gridapi import GridApi

grid = GridApi('http://<grid-uri>', secret=None)

grid.delete_session('<session-id>')

grid.clear_queue()
~~~