## Flask Application Design

### HTML Files

- **index.html:** This file will be the landing page of our application. It will contain basic elements such as a welcome message and instructions for the user.
- **pdf_reader.html:** This file will handle the PDF reading and question-answering functionality. It will have an input field for users to select a PDF file, a button to extract text from the file, and a text area to display the extracted text. It will also incorporate an input field for users to ask their questions and a button to retrieve the answers.
- **results.html:** This file will display the results of the question-answering process. It will include a field to display the question and a field to show the corresponding answer.

### Routes

- **route to display the index page:** This route will serve the `index.html` file when the user first accesses the application.
- **route to read the PDF and display the text:** When the user clicks the "Extract Text" button on the `pdf_reader.html` page, this route will be triggered. It will extract the text from the selected PDF file and display it in the text area on the same page.
- **route to handle question-answering:** When the user enters a question and clicks the "Get Answer" button on the `pdf_reader.html` page, this route will be triggered. It will pass the extracted text and the user's question to the Gemini model for processing. The results, including the question and answer, will be displayed on the `results.html` page.