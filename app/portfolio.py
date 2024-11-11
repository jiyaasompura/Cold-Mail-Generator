import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path="C:/Users/hp/Desktop/cold/app/resource/my_portfolio.csv"):
        # Initialize the Portfolio class with the specified CSV file path
        self.file_path = file_path

        # Load the portfolio data from the CSV file into a DataFrame
        self.data = pd.read_csv(file_path)

        # Initialize the ChromaDB persistent client for vector storage
        self.chroma_client = chromadb.PersistentClient('vectorstore')

        # Create or get the collection named 'portfolio'
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        # Load the portfolio data into the ChromaDB collection if it's empty
        if not self.collection.count():
            for _, row in self.data.iterrows():
                # Add documents to the collection with unique IDs and metadata
                self.collection.add(
                    documents=row["Techstack"],  # The tech stack as the document
                    metadatas={"links": row["Links"]},  # Metadata containing links
                    ids=[str(uuid.uuid4())]  # Generate a unique ID for each document
                )

    def query_links(self, skills):
        # Query the collection for links based on the provided skills
        # Return the metadata of the top n results (here n=2)
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])