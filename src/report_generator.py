from fpdf import FPDF
import datetime
import os
import random
import qrcode


def generate_qr(report_id):
    qr = qrcode.make(f"Facial Paralysis Report ID: {report_id}")
    qr_path = "reports/qr_temp.png"
    qr.save(qr_path)
    return qr_path


def generate_report(
    patient_name,
    age,
    gender,
    diagnosis,
    score,
    severity,
    original_img_path,
    segmented_img_path
):

    report_id = "FP-" + str(random.randint(10000, 99999))
    report_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/assets", exist_ok=True)

    qr_path = generate_qr(report_id)

    pdf = FPDF()
    pdf.add_page()

    # ---------- LOGO ----------
    logo_path = "reports/assets/logo.png"
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=10, y=8, w=25)

    # ---------- HEADER ----------
    pdf.set_xy(40, 10)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(150, 10, "EASTERN MEDICAL DIAGNOSTIC CENTER", ln=True)

    pdf.set_x(40)
    pdf.set_font("Arial", "", 12)
    pdf.cell(150, 8, "AI Facial Paralysis Detection Report", ln=True)

    pdf.ln(10)
    pdf.line(10, 35, 200, 35)

    # ---------- REPORT INFO ----------
    pdf.ln(5)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(100, 8, f"Report ID: {report_id}", border=1)
    pdf.cell(90, 8, f"Date: {report_date}", border=1, ln=True)

    pdf.image(qr_path, x=170, y=40, w=25)

    # ---------- PATIENT DETAILS ----------
    pdf.ln(12)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(200, 8, "Patient Information", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.cell(100, 8, f"Patient Name: {patient_name}", border=1)
    pdf.cell(90, 8, f"Gender: {gender}", border=1, ln=True)

    pdf.cell(100, 8, f"Age: {age}", border=1)
    pdf.cell(90, 8, "Test Type: AI Facial Scan", border=1, ln=True)

    # ---------- IMAGES ----------
    # ---------- IMAGING RESULTS ----------
    pdf.ln(10)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(200, 8, "Imaging Results", ln=True)

    start_y = pdf.get_y() + 2

# Titles
    pdf.set_font("Arial", "B", 11)
    pdf.set_xy(10, start_y)
    pdf.cell(90, 6, "Original Image", align="C")

    pdf.set_xy(110, start_y)
    pdf.cell(90, 6, "Segmentation Output", align="C")

# Images
    img_y = start_y + 8

    if os.path.exists(original_img_path):
        pdf.image(original_img_path, x=10, y=img_y, w=80)

    if os.path.exists(segmented_img_path):
        pdf.image(segmented_img_path, x=110, y=img_y, w=80)

# ⬇️ IMPORTANT: move cursor BELOW images
    pdf.set_y(img_y + 85)


    # ---------- RESULTS ----------
    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(200, 8, "Diagnosis Result", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.cell(190, 8, f"Diagnosis: {diagnosis}", border=1, ln=True)
    pdf.cell(190, 8, f"Asymmetry Score: {score}", border=1, ln=True)
    pdf.cell(190, 8, f"Severity Level: {severity}", border=1, ln=True)

    # ---------- IMPRESSION ----------
    pdf.ln(8)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(200, 8, "Clinical Impression", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(
        190,
        8,
        "Facial asymmetry detected using AI-based landmark and segmentation analysis. "
        "Findings suggest facial nerve involvement. Clinical consultation recommended.",
        border=1
    )

    # ---------- SIGNATURE ----------
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, "Verified By:", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.cell(190, 8, "Dr. A. Sharma (MBBS, Radiology)", border=1, ln=True)
    pdf.cell(190, 8, "Electronic Signature: ____________________", border=1, ln=True)

    # ---------- FOOTER ----------
    pdf.ln(5)
    pdf.set_font("Arial", "I", 9)
    pdf.cell(
        200,
        8,
        "This is an AI-assisted diagnostic report. Final confirmation by clinician is advised.",
        ln=True,
        align="C"
    )

    pdf.output("reports/final_medical_report.pdf")

    if os.path.exists(qr_path):
        os.remove(qr_path)

    print("✅ Full professional medical report generated with images!")
