# Answer Sheet Processing Application

This is a Python application that processes answer sheets in PDF format and retrieves the score and symbol number of students.

## Overview

The Answer Sheet Processing Application allows users to upload answer sheets in PDF format. The application then extracts relevant information, such as the score and symbol number, from the uploaded answer sheets using computer vision techniques. The extracted information is displayed to the user on a result page.

## Directory Structure

The project directory structure is as follows:
app.py
answer_sheets/
answer_sheet_1.pdf
answer_sheet_2.pdf
...
templates/
index.html
result.html


- `app.py`: The main Python file that contains the application code.
- `answer_sheets/`: A directory that stores the answer sheets in PDF format.
- `templates/`: A directory that contains HTML templates for the user interface.

## Setup

To set up and run the application, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install opencv-python PyPDF2 Flask`.
3. Place the answer sheets you want to process in the `answer_sheets/` directory.
4. Run the `app.py` file using Python: `python app.py`.
5. Open your web browser and visit `http://localhost:5000` to access the application.

## Usage

1. Open the application in your web browser.
2. Fill out the form on the home page.
3. Upload an answer sheet in PDF format.
4. Click the "Submit" button.
5. The application will process the answer sheet and display the result page.
6. The result page will show the retrieved score and symbol number for the uploaded answer sheet.

## Dependencies

The Answer Sheet Processing Application relies on the following dependencies:

- OpenCV: A computer vision library for image processing.
- PyPDF2: A library to handle PDF files.
- Flask: A web framework for building the user interface.

These dependencies are listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


