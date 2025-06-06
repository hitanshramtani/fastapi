from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_cost: float = Field(
        ...,
        description="Predicted insurance cost based on user input",
        title="Predicted Insurance Cost",
        example=2000.0
    )
    