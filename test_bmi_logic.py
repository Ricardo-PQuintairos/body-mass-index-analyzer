"""Unit tests for bmi_logic.py — pure functions, no I/O, no database.

Run with:
    pytest tests/
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from bmi_logic import calculate_bmi, classify_bmi, convert_imperial_to_metric


class TestCalculateBmi:
    def test_known_value(self):
        # 70kg, 1.75m -> ~22.86
        assert math.isclose(calculate_bmi(70, 1.75), 22.857, rel_tol=1e-3)

    def test_zero_height_raises(self):
        with pytest.raises(ValueError):
            calculate_bmi(70, 0)

    def test_negative_height_raises(self):
        with pytest.raises(ValueError):
            calculate_bmi(70, -1.75)


class TestClassifyBmi:
    @pytest.mark.parametrize(
        "bmi,expected",
        [
            (17.0, "Underweight"),
            (18.5, "Healthy Weight"),
            (24.9, "Healthy Weight"),
            (25.0, "Overweight"),
            (29.9, "Overweight"),
            (30.0, "Class 1 Obesity"),
            (34.9, "Class 1 Obesity"),
            (35.0, "Class 2 Obesity"),
            (39.9, "Class 2 Obesity"),
            (40.0, "Class 3 Obesity"),
            (50.0, "Class 3 Obesity"),
        ],
    )
    def test_boundaries(self, bmi, expected):
        assert classify_bmi(bmi) == expected


class TestConvertImperialToMetric:
    def test_known_value(self):
        weight_kg, height_m = convert_imperial_to_metric(154, 69)
        assert math.isclose(weight_kg, 69.85, rel_tol=1e-2)
        assert math.isclose(height_m, 1.7526, rel_tol=1e-2)
