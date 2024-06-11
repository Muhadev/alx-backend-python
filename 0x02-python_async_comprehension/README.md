# Python Async Comprehension

This project demonstrates the use of Python's `asyncio` module to create asynchronous generator functions.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Your code should use the pycodestyle style (version 2.5.x)
- The length of your files will be tested using `wc`
- All your modules should have documentation
- All your functions should have documentation
- All your functions and coroutines must be type-annotated

## Task

### 0. Async Generator

Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

Example usage:

```python
#!/usr/bin/env python3

import asyncio
from 0-async_generator import async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
