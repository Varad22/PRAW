**Steps to run thew code:**
1. Create a virtual environment using code: python -m venv env
2. In this virtual environment install the libraries using commands: pip install praw and pip install -q transformers
3. Paste the praw.py file in the virtual env.
4. Now geneate the client_id and client_secret. Refer: https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
5. Now run the code

**Methodology and Challenges Faced**
My approach involved leveraging the PRAW library to access Reddit's API and extract data from the "clinicaltrials" subreddit. Using the Hugging Face Transformers library, I performed sentiment analysis on the comments to gauge user sentiment. One challenge I encountered was handling data cleaning, especially with unstructured text data from Reddit comments. Ensuring that the data was properly formatted and free of unwanted characters was crucial for accurate sentiment analysis.


**Data Collected:** I gathered titles, scores (upvotes) and IDs; and generated URLs using this data of top posts from the "clinicaltrials" subreddit, along with comments and authors from those posts.
**Analysis Performed**: I conducted sentiment analysis on the comments using the Hugging Face Transformers pipeline to classify sentiment as positive, negative, or neutral.
**Messages Generated:** For authors whose comments were classified as positive sentiment, I generated personalized messages encouraging them to consider participating in clinical trials. These messages offered guidance and support throughout the process.

**Ethical Consideration**
In implementing my project, I took a responsible approach by referring to the documentation provided by PRAW for guidance on ethical considerations. By aligning with the guidelines and best practices outlined by the library developers, I ensured that my project respected user privacy, handled data appropriately, and conducted interactions with users ethically.
