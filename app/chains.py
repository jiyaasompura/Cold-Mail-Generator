import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class Chain:
    def __init__(self):
        # Initialize the ChatGroq language model with specified parameters
        self.llm = ChatGroq(
            temperature=0,  # Set temperature for deterministic responses
            groq_api_key=os.getenv("GROQ_API_KEY"),  # Get API key from environment variables
            model_name="llama-3.1-70b-versatile"  # Specify the model to use
        )

    def extract_jobs(self, cleaned_text):
        # Define a prompt template for extracting job postings from scraped text
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        # Combine the prompt with the language model
        chain_extract = prompt_extract | self.llm

        # Invoke the chain to get the response
        res = chain_extract.invoke(input={"page_data": cleaned_text})

        try:
            # Parse the response content as JSON
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
            print(res)  # Print the parsed response
        except OutputParserException:
            # Handle exceptions related to output parsing
            raise OutputParserException("Context too big. Unable to parse jobs.")

        # Return the result as a list of job postings
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links, cv_text):
        # Define a prompt template for writing a cold email
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are [name] take the name from the cv. use this cv which is a pdf to display my skills, projects, and education from: {cv_data}  
            extract the education from the cv which includes the department name
            Your job is to write a cold email to the HR regarding the job mentioned above describing my capability 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase my portfolio: {link_list}
            Remember you are [name] take it from the cv. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        # Combine the prompt with the language model for email generation
        chain_email = prompt_email | self.llm

        # Invoke the chain to generate the email content
        res = chain_email.invoke({"job_description": str(job), "link_list": links, "cv_data": cv_text})
        return res.content  # Return the generated email content


if __name__ == "__main__":
    # Print the API key to verify it's loaded correctly (for debugging purposes)
    print(os.getenv("GROQ_API_KEY"))