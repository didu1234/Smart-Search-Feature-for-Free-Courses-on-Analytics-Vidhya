# Smart-Search-Feature-for-Free-Courses-on-Analytics-Vidhya
Smart Search Feature for Free Courses on Analytics Vidhya

1. Objective
The goal of this project is to create a smart search feature for free courses on the Analytics Vidhya platform. This feature will help users find relevant courses by understanding the meaning behind their search query, not just matching keywords. We use BERT, a machine learning model, to achieve this.

3. How We Collected Course Data
To get information about the free courses, we used a technique called web scraping. Here's how it works:
We fetched the webpage that lists the free courses.
We used a tool called BeautifulSoup to extract important details about each course, such as:
            Course Title: The name of the course.
            Course Image: The image associated with the course.
            Course Link: The link to the full course.
4. How the Search Works
When a user types a search query (e.g. "data science")the system:

Converts the search query into embeddings.
Compares those embeddings with the embeddings of the course titles.
Ranks the courses based on how similar they are to the query, and shows the most relevant results.

5. Understanding BERT for Search
BERT is a model that understands the context of words in a sentence. This is useful for matching the meaning of the words in a search query with the titles of the courses.
How BERT is used:
For each course title, we convert the title into a set of numbers called embeddings using BERT.
When a user types a search query, we also convert that query into embeddings.
We then compare the embeddings of the query and the courses to see which courses are most similar to the query.

6. How the Search Works
When a user types a search query (e.g "data science") the system:
Converts the search query into embeddings.
Compares those embeddings with the embeddings of the course titles.
Ranks the courses based on how similar they are to the query, and shows the most relevant results.

7. Autocomplete Functionality
To make the search process faster, we also added autocomplete. This means that as the user types, we show them suggestions based on course titles that match what they have typed so far. It helps the user refine their search before they even press enter.

9. Building the User Interface
We created a simple, user-friendly interface using Gradio, a tool that lets us easily build and deploy web interfaces for machine learning models. The interface allows users to:
Type their search query.
See the results immediately, including the course title, image, and link.
Key Features:
The courses are displayed in cards, with the course image, title, and relevance score.
Users can click on the course link to view the course details.

10. Deployment
Once everything was set up, we deployed the tool online using Gradio. This means anyone can access it via a web link, and they can search for courses in real-time.

11. Conclusion
This smart search tool makes it easy for users to find relevant free courses on Analytics Vidhya. By using BERT to understand the meaning behind the search queries, the system provides more accurate results compared to traditional keyword-based search engines.

