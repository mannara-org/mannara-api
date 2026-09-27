
def main() -> None:
    import uvicorn
    uvicorn.run("mannara_api.main:app", reload=True)
