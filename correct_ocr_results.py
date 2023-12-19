import re

def correct_ocr_results(text):
    if 'pm' in text.lower() or 'am' in text.lower():
        text = re.sub(r'(\d+): ?(\d+)([ap]m)', r'\1:\2\3', text)  # Correct spaces in time format
        text = re.sub(r'Latest (\d+).(\d+)([ap]m)', r'Latest \1:\2\3', text)
        text = re.sub(r'(\d{2})\.(\d{2})\.(\d{2})([ap]m)', r'\1:\2:\3\4', text)
        text = re.sub(r'I1', '11', text)  # Correct common OCR mistake for 11
        text = re.sub(r'IO', '10', text)  # Correct common OCR mistake for 10
        text = re.sub(r'I5', '15', text)  # Correct common OCR mistake for 10
        text = re.sub(r'4O', '40', text)  # Correct common OCR mistake for 40
        text = re.sub(r'O', '0', text)    # Correct common OCR mistake for 0

        # Additional correction for time format with dots
        text = re.sub(r'(\d+)\.(\d+)([ap]m)', r'\1:\2\3', text)

        text = re.sub(r'(\d+\.\d{1,2})1b', r'\1lb', text)

    text = re.sub(r'(\d+\.\d{1,2})1b', r'\1lb', text)

    # Correct Celsius symbol
    text = re.sub(r'(\d+)8C', r'\1°C', text)
    text = re.sub(r'(\d+)9C', r'\1°C', text)
    text = re.sub(r'(\d+)PC', r'\1°C', text)
    text = re.sub(r'(\d+)8€', r'\1°C', text)

    # Correct mg/dL format
    text = re.sub(r'mgldL', 'mg/dL', text)

    # Correct L/min/m? format with a preceding number
    text = re.sub(r'(\d+(\.\d+)?)Lmin/m\?', r'\1L/min/m²', text)

    # Retain only numeric values on the right side of ">X%:"
    text = re.sub(r'Drops >(\d+)%[: ]*(\d+)', r'\2', text)
    text = re.sub(r'Drops >(\d+)%[; ]*(\d+)', r'\2', text)
    text = re.sub(r'Drops >(\d+)%[: ]*>\s*(\d+)', r'\2', text)

    # Remove prefix "Drops over 3%." and retain text after the dot
    text = re.sub(r'Drops over \d+\%.(\d+)', r'\1', text)

    # Correct decimal numbers with commas
    text = re.sub(r'(\d+),(\d+)', r'\1.\2', text)

    return text