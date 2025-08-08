from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the CUB Benchmark Space. This is a placeholder for the benchmark application."}
