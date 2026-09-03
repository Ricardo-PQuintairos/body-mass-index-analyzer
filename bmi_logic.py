"""Pure business logic for BMI calculation and classification.

These functions contain no I/O (no input(), no print(), no database or
file access), which makes them trivial to unit test in isolation.
"""


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI (kg/m^2) from weight in kilograms and height in meters.

    Raises:
        ValueError: if height_m is not strictly positive.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than 0.")
    return weight_kg / height_m ** 2


def classify_bmi(bmi: float) -> str:
    """Classify a BMI value into a standard WHO-style category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy Weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Class 1 Obesity"
    elif bmi < 40:
        return "Class 2 Obesity"
    else:
        return "Class 3 Obesity"


def convert_imperial_to_metric(weight_lbs: float, height_in: float) -> tuple[float, float]:
    """Convert weight (lbs) and height (inches) to (weight_kg, height_m)."""
    weight_kg = weight_lbs * 0.453592
    height_m = height_in * 0.0254
    return weight_kg, height_m
