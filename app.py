from fastapi import FastAPI, HTTPException , Request,Form
import pandas as pd
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from schema.user_input import UserInput
from model.predict import MODEL_VERSION, predict_output,model
from schema.prediction_response import PredictionResponse
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Allow CORS if frontend is separate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates dir
templates = Jinja2Templates(directory="templates")

# Show form at root
@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    logger.info("Rendering index.html")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    if model is None:
        logger.error("Model is not loaded")
        return JSONResponse(
            content={"status": "ERROR", "message": "Model not loaded"},
            status_code=500
        )
    return{
        "status": "OK",
        "message": "API is running smoothly",
        "version": MODEL_VERSION,
        "model_loaded": True if model else False
    }



@app.post("/predict", response_model=PredictionResponse)
def predict_insurance_cost(data: UserInput):
    try:
        logger.info(f"Received data for prediction: {data.model_dump()}")
        df = pd.DataFrame([data.model_dump()])
        df['bmi'] = data.bmi
        df = df.drop(columns=["Height", "Weight"])
        prediction = predict_output(df)
        logger.info(f"Prediction made: {prediction[0]}")
        return JSONResponse(content={"predicted_cost": float(prediction[0])},status_code=200)
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
    
    
    