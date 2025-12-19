# Users

Types:

```python
from userplex.types import UserIdentifyResponse
```

Methods:

- <code title="post /api/identify">client.users.<a href="./src/userplex/resources/users.py">identify</a>(\*\*<a href="src/userplex/types/user_identify_params.py">params</a>) -> <a href="./src/userplex/types/user_identify_response.py">UserIdentifyResponse</a></code>

# Logs

Types:

```python
from userplex.types import LogBatchResponse, LogNewResponse
```

Methods:

- <code title="post /api/logs/batch">client.logs.<a href="./src/userplex/resources/logs.py">batch</a>(\*\*<a href="src/userplex/types/log_batch_params.py">params</a>) -> <a href="./src/userplex/types/log_batch_response.py">LogBatchResponse</a></code>
- <code title="post /api/log">client.logs.<a href="./src/userplex/resources/logs.py">new</a>(\*\*<a href="src/userplex/types/log_new_params.py">params</a>) -> <a href="./src/userplex/types/log_new_response.py">LogNewResponse</a></code>
