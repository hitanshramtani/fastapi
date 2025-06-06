from pydantic import BaseModel, Field, computed_field ,field_validator
from typing import Optional, List, Literal, Annotated, Dict
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt = 0,lt = 100, title="Age of the User", description="Age should be between 1 and 99", example=30)]
    sex: Annotated[Literal["male","female"], Field(..., title = "Sex of the User", description = "Either Male or Female")]
    Height: Annotated[float, Field(..., gt = 0, lt = 2.6, title="Height of the User", description="Height in meters", example=1.75)]
    Weight: Annotated[float, Field(..., gt = 0, lt = 600, title="Weight of the User", description="Weight in kilograms", example=70.5)]
    children: Annotated[int, Field(..., ge = 0, le = 5, title="Number of Children", description="Number of children the user has", example=2)]
    smoker: Annotated[Literal["yes", "no"], Field(..., title="Smoking Status", description="Whether the user is a smoker or not", example="no")]
    region: Annotated[Literal["northeast", "northwest", "southeast", "southwest"], Field(..., title="Region", description="Geographical region of the user", example="northeast")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.Weight / (self.Height ** 2), 2)
        return bmi
    @field_validator("sex", "smoker", "region", mode="before")
    @classmethod
    def lowercase_strings(cls, v:str) -> str:
        """thiis function lowers the string so that it can validate the data correctly without case sensitivity"""
        return v.strip().lower()