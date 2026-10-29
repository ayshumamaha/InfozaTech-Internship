"""INFOZATECH Task 3: BMI Calculator
Run with: python task3_bmi_calculator.py
BMI is a screening measure, not a diagnosis.
"""
import json
from datetime import datetime
from pathlib import Path

HISTORY_FILE = Path(__file__).with_name("bmi_history.json")


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Healthy weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity"


def save_record(record):
    try:
        if HISTORY_FILE.exists():
            try:
                records = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
                if not isinstance(records, list):
                    records = []
            except json.JSONDecodeError:
                records = []
        else:
            records = []
        records.append(record)
        HISTORY_FILE.write_text(json.dumps(records, indent=4), encoding="utf-8")
    except OSError as error:
        print(f"Could not save BMI history: {error}")


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("===== BMI CALCULATOR =====")
    print("Choose units: 1. Metric (kg, cm)  2. Imperial (lb, inches)")
    unit = input("Enter 1 or 2: ").strip()

    if unit == "1":
        weight = get_positive_number("Weight in kilograms: ")
        height_cm = get_positive_number("Height in centimetres: ")
        height_m = height_cm / 100
        weight_kg = weight
    elif unit == "2":
        weight_lb = get_positive_number("Weight in pounds: ")
        height_in = get_positive_number("Height in inches: ")
        weight_kg = weight_lb * 0.45359237
        height_m = height_in * 0.0254
    else:
        print("Invalid unit selection.")
        return

    bmi = weight_kg / (height_m ** 2)
    category = classify_bmi(bmi)
    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Adult BMI category: {category}")
    print("Note: BMI is a screening measure and does not replace professional medical advice.")

    record = {
        "date": datetime.now().isoformat(timespec="seconds"),
        "weight_kg": round(weight_kg, 2),
        "height_m": round(height_m, 3),
        "bmi": round(bmi, 2),
        "category": category,
    }
    save_record(record)


if __name__ == "__main__":
    main()
