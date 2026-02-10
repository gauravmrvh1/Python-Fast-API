Uvicorn = FastAPI ke liye web server


ASGI = Asynchronous Server Gateway Interface
    - async / await support
    - high concurrency
    - WebSockets support


python -m uvicorn main:app --reload
-------------------------------
| Part     | Meaning          |
| -------- | ---------------- |
| python   | interpreter      |
| -m       | module run       |
| uvicorn  | ASGI server      |
| main     | file name        |
| app      | FastAPI instance |
| --reload | auto restart     |
-------------------------------


(here we have renamed file from main.py to server.py)

python -m uvicorn server:app --reload 