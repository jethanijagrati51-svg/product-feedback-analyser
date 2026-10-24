# Product Feedback Analyser

A Python-based web application that analyses customer reviews to identify common themes, pain points, and potential product improvements.

## About the Project

Customer reviews contain valuable information about what users like, what frustrates them, and what they want improved. However, manually reading a large number of reviews can be time-consuming.

The Product Feedback Analyser helps organize review feedback into meaningful categories and suggests possible improvements, making it easier to understand customer needs.

## Features

- **Review Analysis:** Processes customer review text.
- **Theme Detection:** Identifies themes such as customer support based on keywords in reviews.
- **Pain Point Identification:** Highlights potential problems experienced by customers.
- **Feature Suggestions:** Generates suggestions related to detected issues.
- **Web Interface:** Provides a frontend built with HTML, CSS, and JavaScript.
- **Python Backend:** Handles review analysis and application logic.

## Technologies Used

- Python
- Flask (if used by the application)
- HTML
- CSS
- JavaScript
- SQLite (if used by the application)
- Git and GitHub

## Project Structure

```text
product-feedback-backend/
├── app.py
├── analyzer.py
├── database.py
├── seed.py
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .gitignore
└── README.md
```

## How It Works

1. Customer review text is provided to the application.
2. The backend processes the review.
3. The analyser identifies matching themes and potential pain points.
4. Relevant feature suggestions are generated.
5. The results can be displayed through the frontend.

## Getting Started

### Prerequisites

- Python 3 installed
- Git installed
- Visual Studio Code (recommended)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/jethanijagrati51-svg/product-feedback-analyser.git
   ```

2. Open the project folder:

   ```bash
   cd product-feedback-analyser
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the environment on Windows:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install the required packages using `requirements.txt` once it has been created:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the application using the appropriate command for your Flask setup. For example, if `app.py` defines the Flask application:

   ```bash
   python app.py
   ```

7. Open the local URL shown in your terminal.

## Future Improvements

- Integrate AI or natural language processing for deeper review analysis.
- Add sentiment analysis to classify positive, negative, and neutral feedback.
- Rank pain points by frequency and customer impact.
- Build a dashboard to visualize trends across reviews.
- Support exporting analysis results to CSV.
- Add review-source integrations where APIs are available.

## Learning Outcomes

This project demonstrates practical learning in Python programming, web development, text processing, database handling, and product thinking.

## Author

**Jagrati Jethani**

GitHub: [@jethanijagrati51-svg](https://github.com/jethanijagrati51-svg)

---

This project is developed for learning and portfolio purposes.
