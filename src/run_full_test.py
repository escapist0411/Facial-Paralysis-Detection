from src.predict import predict_image
from src.report_generator import generate_report


def main():
	img_path = "dataset/test/sample.jpg"

	result, score, severity, confidence = predict_image(img_path)

	# generate_report expects many parameters; this example call is left as a
	# placeholder for manual invocation. When used as a script it may be
	# extended to pass patient details and image paths to `generate_report`.
	# generate_report(result, score, severity)


if __name__ == "__main__":
	main()

