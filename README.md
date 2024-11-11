# Cold Mail Generator

A powerful Python-based tool designed to streamline the creation of personalized cold emails. By leveraging **LangChain** and **ChromaDB**, this tool automatically extracts relevant information from job postings, user CVs, and portfolios to generate professional cold emails that can be sent to potential employers, clients, or partners.

---

## Features

- **Job Extraction**: Automatically extracts job details (skills, role, experience) from a given URL (e.g., job listings or career pages).
- **CV Parsing**: Upload a CV (in PDF format), and the system will extract the relevant text, including educational background and skills.
- **Portfolio Integration**: Use your portfolio data (in CSV format) to enrich your cold emails with relevant links showcasing your work.
- **Cold Email Generation**: Based on the extracted job information, CV, and portfolio links, the tool generates a personalized cold email.
- **Customizable & Scalable**: Easily adjust the workflow for different use cases like job applications, sales outreach, or networking.

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Cold-Mail-Generator.git
cd Cold-Mail-Generator
```

### 2. Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install the necessary libraries, including **Streamlit**, **LangChain**, **ChromaDB**, and others.

### 3. Set Up Environment Variables

You will need an API key for **Groq** (used for the ChatGroq language model). Create a `.env` file in the root directory of the project and add the following:

```
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

---

## Usage

### 1. Run the Streamlit App

To start the app, simply run the following command in your terminal:

```bash
streamlit run app.py
```

### 2. Upload Your CV

- In the app, upload your CV in PDF format. The system will extract key details, such as your education, skills, and other relevant information.

### 3. Enter the URL

- Input a URL (e.g., a job listing or company career page). The tool will scrape the page to extract job details like job roles, required skills, and experience levels.

### 4. Generate Cold Email

- Once the data is loaded, the tool will generate a personalized cold email based on your CV, the job description, and links from your portfolio.

### Example Cold Email Output:

```text
Subject: Application for Software Engineer Role

Dear [Hiring Manager’s Name],

I hope this email finds you well. I am writing to express my interest in the Software Engineer position at [Company Name] as posted on your careers page.

With my background in [your tech stack, e.g., Python, JavaScript, Machine Learning] and a degree in [Your Degree] from [University Name], I believe I can contribute effectively to your team.

Please find my relevant work showcased here:
- [Portfolio Link 1]
- [Portfolio Link 2]

Looking forward to the opportunity to discuss how I can contribute to your team.

Best regards,  
[Your Name]  
[Your Contact Information]
```

---

## How It Works

1. **Job Information Extraction**:
   The tool uses **LangChain's** `ChatGroq` model to scrape and extract job details such as role, required skills, experience, and description from the provided URL.

2. **CV Parsing**:
   The uploaded CV is processed using **LangChain's** PDF loader to extract text, which is then cleaned to remove any unnecessary formatting.

3. **Portfolio Integration**:
   The portfolio CSV file (which includes the user's tech stack and portfolio links) is loaded into **ChromaDB**, a vector database used to store and query documents. Based on the job skills extracted, relevant portfolio links are retrieved and incorporated into the generated email.

4. **Cold Email Generation**:
   The final step is the generation of a cold email using the extracted job details, CV content, and portfolio links. The email is returned as a formatted string ready for sending.

---

## Code Structure

Here’s a brief overview of the project structure:

```text
Cold-Mail-Generator/
├── app.py                # Main Streamlit app file
├── portfolio.py          # Handles loading and querying the portfolio data
├── chains.py             # Contains logic for job extraction and cold email generation
├── utils.py              # Utility functions, such as text cleaning
├── requirements.txt      # Required Python packages
├── .env                  # Store environment variables (e.g., API keys)
├── my_portfolio.csv      # Example portfolio data (CSV format)
└── README.md             # This README file
```

### Key Classes:

- **Chain**: Responsible for extracting job information and generating cold emails using **LangChain**.
- **Portfolio**: Manages portfolio data, integrates with **ChromaDB** for storing and querying portfolio links based on the user’s skills.
- **Utils**: Contains utility functions like `clean_text` for sanitizing the scraped and extracted text.

---

## Contributing

Contributions to this project are welcome! If you want to help improve this tool, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Streamlit**: For providing the framework for building interactive web apps.
- **LangChain**: For simplifying NLP workflows and enabling powerful language model applications.
- **ChromaDB**: For providing fast, persistent vector storage and similarity search.
