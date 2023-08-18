
import uvicorn
from fastapi import FastAPI

#: Web services
app = FastAPI()


@app.get("/dosomething")
async def dosomething( x: int, y: int ) -> int:
	return {'sum': x+y}

#: Run
if __name__ == '__main__':
	uvicorn.run(
		"fastapiexample:app",
		host="0.0.0.0",
		port=5700,
		log_level="debug",
		reload=True,
	)
	