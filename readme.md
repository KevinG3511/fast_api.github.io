python -m venv .venv

pip install "fastapi[all]"

pip install "uvicorn[standard]"

create main.py
            from fastapi import FastAPI

            app = FastAPI()


            @app.get("/")
            async def root():
                return {"message": "Hello World"}

uvicorn main:app --reload
