from get_sleep_hours import get_sleep_hours
import re

def get_numeric_value(value, pattern):
    return re.sub(pattern, '', value).strip()

def get_sleep_minutes(input_str):
    start_time, end_time = input_str.split("-")

    def convert_to_24_hour(time):
        hours, minutes = map(int, time[:-2].split(":"))
        period = time[-2:].lower()

        if period == "pm" and hours != 12:
            hours += 12
        elif period == "am" and hours == 12:
            hours = 0

        return hours, minutes

    start = convert_to_24_hour(start_time)
    end = convert_to_24_hour(end_time)

    hours_diff = end[0] - start[0]
    minutes_diff = end[1] - start[1]

    if minutes_diff < 0:
        minutes_diff += 60
        hours_diff -= 1

    if hours_diff < 0:
        hours_diff += 24

    return hours_diff * 60 + minutes_diff

def dashboard_data(result):
    total_dailySteps = result[0]
    total_dalySleep = result[1]
    medical_report = [
        {
            "diagnosis": "Pedometer",
            "diagnosis_label": result[2],
            "diagnosis_value": result[3],
            "diagnosis_keyValue": "steps",
            "diagnosis_numeric_value": get_numeric_value(result[3], 'Steps'),
        },
        {
            "diagnosis": "Sleep",
            "diagnosis_label": get_sleep_hours(result[4]),
            "diagnosis_value": result[4],
            "diagnosis_keyValue": "hours",
            "diagnosis_numeric_value": str(get_sleep_minutes(result[4])),
        },
        {
            "diagnosis": "Heart Rate",
            "diagnosis_label": result[5],
            "diagnosis_value": result[6],
            "diagnosis_keyValue": "bpm",
            "diagnosis_numeric_value": get_numeric_value(result[6], 'bpm'),
        },
        {
            "diagnosis": "Blood Pressure",
            "diagnosis_label": result[7],
            "diagnosis_value": result[8],
            "diagnosis_keyValue": "mmHg",
            "diagnosis_numeric_value": get_numeric_value(result[8], 'mmHg'),
        },
        {
            "diagnosis": "Blood Oxygen",
            "diagnosis_label": result[9],
            "diagnosis_value": result[10],
            "diagnosis_keyValue": "percentage",
            "diagnosis_numeric_value": get_numeric_value(result[10], '%'),
        },
        {
            "diagnosis": "HRV",
            "diagnosis_label": result[11],
            "diagnosis_value": result[12],
            "diagnosis_keyValue": "",
            "diagnosis_keyValue": result[12],
        },
        {
            "diagnosis": "Body Temperature",
            "diagnosis_label": result[13],
            "diagnosis_value": result[14],
            "diagnosis_keyValue": "celcius",
            "diagnosis_numeric_value": get_numeric_value(result[14], '°C'),
        },
        {
            "diagnosis": "Blood Glucose",
            "diagnosis_label": result[15],
            "diagnosis_value": result[16],
            "diagnosis_keyValue": "mg/dL",
            "diagnosis_numeric_value": get_numeric_value(result[16], 'mg/dL|mmol/L'),
        }
    ]

    return total_dailySteps, total_dalySleep, medical_report

def bmi_data(result):
    average_weight = result[0]
    status = result[1]
    medical_record = [
        {
            "diagnosis_label": "Weight",
            "diagnosis_value": result[2],
            "diagnosis_status": result[3],
        },
        {
            "diagnosis_label": "Body Fat",
            "diagnosis_value": result[4],
            "diagnosis_status": result[5],
        },
        {
            "diagnosis_label": "BMI",
            "diagnosis_value": result[6],
            "diagnosis_status": result[7],
        },
        {
            "diagnosis_label": "Skeletal Muscle",
            "diagnosis_value": result[8],
            "diagnosis_status": result[9],
        },
        {
            "diagnosis_label": "Muscle Mass",
            "diagnosis_value": result[10],
            "diagnosis_status": result[11],
        },
        {
            "diagnosis_label": "Protein",
            "diagnosis_value": result[12],
            "diagnosis_status": result[13],
        },
        {
            "diagnosis_label": "BMR",
            "diagnosis_value": result[14],
            "diagnosis_status": result[15],
        },
        {
            "diagnosis_label": "Fat Free Body Weight",
            "diagnosis_value": result[16],
            "diagnosis_status": result[17],
        },
        {
            "diagnosis_label": "Subcutaneous Fat",
            "diagnosis_value": result[18],
            "diagnosis_status": result[19],
        },
        {
            "diagnosis_label": "Visceral Fat",
            "diagnosis_value": result[20],
            "diagnosis_status": result[21],
        },
        {
            "diagnosis_label": "Body Water",
            "diagnosis_value": result[22],
            "diagnosis_status": result[23],
        },
        {
            "diagnosis_label": "Bone Mass",
            "diagnosis_value": result[24],
            "diagnosis_status": result[25],
        },
        {
            "diagnosis_label": "Heart Rate",
            "diagnosis_value": result[26],
            "diagnosis_status": result[27],
        },
        {
            "diagnosis_label": "Cardiac Index",
            "diagnosis_value": result[28],
            "diagnosis_status": result[29],
        },
        {
            "diagnosis_label": "Metabolic Age",
            "diagnosis_value": result[30],
            "diagnosis_status": result[31],
        },
    ]
    return average_weight, status, medical_record

def ring_data(result):
    return {
        "oxygen_level": result[0],
        "pulse_rate": result[1],
        "o2_score": result[2],
    }
