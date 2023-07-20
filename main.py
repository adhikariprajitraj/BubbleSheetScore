import cv2
import PyPDF2
from flask import Flask, render_template, request

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    # Get the uploaded file from the form
    file = request.files['answer_sheet']

    # Extract the image from the PDF
    pdf_reader = PyPDF2.PdfReader(file)
    page = pdf_reader.pages[0]  # Assuming the answer sheet is on the first page
    img = page.to_image()

    # Convert the image to grayscale for processing
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply image processing techniques to extract relevant information
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_gray = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    img_gray = cv2.bitwise_not(img_gray)
    

    # Calculate the score and extract the symbol number from the processed image
    score = calculate_score(img_gray)
    symbol_number = extract_symbol_number(img_gray)

    # Return the result page
    return render_template('result.html', score=score, symbol_number=symbol_number)


if __name__ == '__main__':
    app.run(debug=True)
