from get_sleep_hours import get_sleep_hours

def dashboard_data(result):
    total_dailySteps = result[0]
    total_dalySleep = result[1]
    medical_report = [
        {
            "diagnosis": "Pedometer",
            "diagnosis_label": result[2],
            "diagnosis_value": result[3],
            "diagnosis_keyValue": "steps",
        },
        {
            "diagnosis": "Sleep",
            "diagnosis_label": get_sleep_hours(result[4]),
            "diagnosis_value": result[4],
            "diagnosis_keyValue": "hours",
        },
        {
            "diagnosis": "Heart Rate",
            "diagnosis_label": result[5],
            "diagnosis_value": result[6],
            "diagnosis_keyValue": "bp",
        },
        {
            "diagnosis": "Blood Pressure",
            "diagnosis_label": result[7],
            "diagnosis_value": result[8],
            "diagnosis_keyValue": "mmHg",
        },
        {
            "diagnosis": "Blood Oxygen",
            "diagnosis_label": result[9],
            "diagnosis_value": result[10],
            "diagnosis_keyValue": "percentage",
        },
        {
            "diagnosis": "HRV",
            "diagnosis_label": result[11],
            "diagnosis_value": result[12],
            "diagnosis_keyValue": "",
        },
        {
            "diagnosis": "Body Temperature",
            "diagnosis_label": result[13],
            "diagnosis_value": result[14],
            "diagnosis_keyValue": "celcius",
        },
        {
            "diagnosis": "Blood Glucose",
            "diagnosis_label": result[15],
            "diagnosis_value": result[16],
            "diagnosis_keyValue": "mg/dL",
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
