# src/severity_classifier.py

def severity_level(score, confidence=0.0, label="Normal"):

    if label == "Normal":
        return "Normal"

    # Base severity on confidence level as requested
    if confidence > 0.95:
        return "Severe Paralysis"

    elif confidence > 0.80:
        return "Moderate Paralysis"

    else:
        return "Mild Paralysis"



# Quick test (Run this file directly)
if __name__ == "__main__":
    print("Test Severity Output:", severity_level(7))
