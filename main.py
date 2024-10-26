from fastapi import FastAPI
from routes import user_routes, auth_routes


app = FastAPI()

# Include routes
app.include_router(user_routes.router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
