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
            "diagnosis_label": result[3],
            "diagnosis_value": result[4],
            "diagnosis_keyValue": "steps",
            "diagnosis_numeric_value": get_numeric_value(result[4], 'Steps'),
        },
        {
            "diagnosis": "Sleep",
            "diagnosis_label": get_sleep_hours(result[6]),
            "diagnosis_value": result[6],
            "diagnosis_keyValue": "hours",
            "diagnosis_numeric_value": str(get_sleep_minutes(result[6])),
        },
        {
            "diagnosis": "Heart Rate",
            "diagnosis_label": result[8],
            "diagnosis_value": result[9],
            "diagnosis_keyValue": "bpm",
            "diagnosis_numeric_value": get_numeric_value(result[9], 'bpm'),
        },
        {
            "diagnosis": "Blood Pressure",
            "diagnosis_label": result[11],
            "diagnosis_value": result[12],
            "diagnosis_keyValue": "mmHg",
            "diagnosis_numeric_value": get_numeric_value(result[12], 'mmHg'),
        },
        {
            "diagnosis": "Blood Oxygen",
            "diagnosis_label": result[14],
            "diagnosis_value": result[15],
            "diagnosis_keyValue": "percentage",
            "diagnosis_numeric_value": get_numeric_value(result[15], '%'),
        },
        {
            "diagnosis": "HRV",
            "diagnosis_label": result[17],
            "diagnosis_value": result[18],
            "diagnosis_keyValue": "",
            "diagnosis_keyValue": result[18],
        },
        {
            "diagnosis": "Body Temperature",
            "diagnosis_label": result[20],
            "diagnosis_value": result[21],
            "diagnosis_keyValue": "celcius",
            "diagnosis_numeric_value": get_numeric_value(result[21], '°C'),
        },
        {
            "diagnosis": "Blood Glucose",
            "diagnosis_label": result[23],
            "diagnosis_value": result[24],
            "diagnosis_keyValue": "mg/dL",
            "diagnosis_numeric_value": get_numeric_value(result[24], 'mg/dL|mmol/L'),
        }
    ]

    return total_dailySteps, total_dalySleep, medical_report

def watch_data(raw_data):
    data = format_watch_region_label(raw_data)
    diagnosis_keys = ['Pedometer', 'Sleep', 'Heart Rate', 'Blood pressure', 'Blood oxygen', 'HRV', 'ECG', 'Body temperature', 'Blood Glucose']
    key_values = ['Steps', 'hours', 'bpm', 'mmHg', '%', '', '', '°C', 'mg/dL', 'mmol/L']
    
    total_dailySteps = data[0]
    total_dailySleep = data[1]
    medical_report = []
    
    for i in range(2, len(data)):
        if data[i] in diagnosis_keys:
            index = diagnosis_keys.index(data[i])
            diagnosis_value = data[i+2]
            sleep_value = data[i+1]
            diagnosis = {
                "diagnosis": data[i],
                "diagnosis_label": data[i+1],
                "diagnosis_keyValue": key_values[index],
            }

            if diagnosis["diagnosis"] == 'Sleep':
               diagnosis["diagnosis_label"] = get_sleep_hours(data[i+1])
               diagnosis["diagnosis_value"]= sleep_value
               diagnosis["diagnosis_numeric_value"] = str(get_sleep_minutes(sleep_value))
            else:
                key_pattern = key_values[index]

                if diagnosis_value in diagnosis_keys:
                    diagnosis["diagnosis_numeric_value"] = ""
                    diagnosis["diagnosis_value"]= ""
                else:
                    diagnosis["diagnosis_numeric_value"] = get_numeric_value(diagnosis_value, key_pattern)
                    diagnosis["diagnosis_value"]= diagnosis_value

            medical_report.append(diagnosis)
            
    return total_dailySteps, total_dailySleep, medical_report

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


def format_watch_region_label(lst):
      # Find the index of 'Body'
    body_index = lst.index('Body')
    # Combine 'Body' and 'temperature' into 'Body temperature'
    lst[body_index] = lst[body_index] + ' ' + lst[body_index + 1]
    # Remove 'temperature' from the list
    del lst[body_index + 1]
    return lst