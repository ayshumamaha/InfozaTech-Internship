# BMI Calculator

## Overview
The BMI Calculator is a Python application that calculates Body Mass Index (BMI) using a person's height and weight. It supports metric and imperial measurements and displays the corresponding adult BMI category.

## Features
- Accept weight in kilograms or pounds.
- Accept height in centimetres or inches.
- Convert measurements into standard units.
- Calculate BMI.
- Display the BMI value and category.
- Save calculation history in a JSON file.
- Validate numerical inputs.

## BMI Formula

BMI is calculated using the following formula:

`BMI = Weight (kg) / [Height (m) × Height (m)]`

## Adult BMI Categories
- Below 18.5: Underweight
- 18.5 to below 25: Healthy weight
- 25 to below 30: Overweight
- 30 and above: Obesity

## Technologies Used
- Python 3
- json
- datetime
- pathlib

## How to Run

```bash
python task3_bmi_calculator.py
```

## Data Storage
BMI records are saved in `bmi_history.json`.

## Concepts Used
Arithmetic operations, functions, conditional statements, input validation, unit conversion, and file handling.

## Note
BMI is a screening measure and does not replace professional medical assessment.

## Conclusion
This project demonstrates the use of Python for calculations, input validation, and persistent record storage.

## Author
**M. Ayshwarya**
