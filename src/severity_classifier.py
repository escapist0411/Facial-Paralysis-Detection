# src/severity_classifier.py

def severity_level(score):

    if score < 2:
        return "Normal"

    elif score < 5:
        return "Mild Paralysis"

    elif score < 10:
        return "Moderate Paralysis"

    else:
        return "Severe Paralysis"



# Quick test (Run this file directly)
if __name__ == "__main__":
    print("Test Severity Output:", severity_level(7))
