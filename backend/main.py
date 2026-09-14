from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"backend": "ok", "application": "incident-ai-assistant"}
