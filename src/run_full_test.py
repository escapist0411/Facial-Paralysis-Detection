from src.predict import predict_image
from src.report_generator import generate_report

img_path = "dataset/test/sample.jpg"

result, score, severity = predict_image(img_path)

generate_report(result, score, severity)

