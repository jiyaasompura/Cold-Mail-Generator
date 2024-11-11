import re


def clean_text(text):
    # Remove HTML tags from the text
    text = re.sub(r'<[^>]*?>', '', text)

    # Remove URLs from the text
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

    # Remove special characters, keeping only alphanumeric characters and spaces
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    # Replace multiple consecutive spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)

    # Trim leading and trailing whitespace from the text
    text = text.strip()

    return text  # Return the cleaned text