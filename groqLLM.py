import requests
from bs4 import BeautifulSoup
import pandas as pd
import gradio as gr
from fuzzywuzzy import process # type: ignore

# Placeholder data for suggestions
example_suggestions = [
    "machine learning", 
    "python for data science", 
    "deep learning", 
    "statistics for beginners", 
    "data visualization"
]

# Search Function
def gradio_search(query):
    # Replace with actual course search logic
    results = [
        {"title": "Machine Learning Basics", "image_url": "https://via.placeholder.com/150", "course_link": "#", "score": 0.95},
        {"title": "Deep Learning Fundamentals", "image_url": "https://via.placeholder.com/150", "course_link": "#", "score": 0.90},
    ]
    if query.lower() not in [s.lower() for s in example_suggestions]:
        return '<p class="no-results">No results found. Please try a different query.</p>'
    
    html_output = '<div class="results-container">'
    for item in results:
        course_title = item['title']
        course_image = item['image_url']
        course_link = item['course_link']
        relevance_score = round(item['score'] * 100, 2)
        html_output += f'''
        <div class="course-card">
            <img src="{course_image}" alt="{course_title}" class="course-image"/>
            <div class="course-info">
                <h3>{course_title}</h3>
                <p>Relevance: {relevance_score}%</p>
                <a href="{course_link}" target="_blank" class="course-link">View Course</a>
            </div>
        </div>'''
    html_output += '</div>'
    return html_output

# CSS for improved layout
custom_css = """
body {
    font-family: Arial, sans-serif;
    background-color: #f0f2f5;
}
.results-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.course-card {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    overflow: hidden;
    width: 48%;
    transition: transform 0.2s;
}
.course-card:hover {
    transform: translateY(-5px);
}
.course-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
}
.course-info {
    padding: 15px;
}
.course-info h3 {
    margin-top: 0;
    font-size: 18px;
    color: #333;
}
.course-info p {
    color: #666;
    font-size: 14px;
    margin-bottom: 10px;
}
.course-link {
    display: inline-block;
    background-color: #007bff;
    color: white;
    padding: 8px 12px;
    text-decoration: none;
    border-radius: 4px;
    font-size: 14px;
    transition: background-color 0.2s;
}
.course-link:hover {
    background-color: #0056b3;
}
.no-results {
    text-align: center;
    color: #666;
    font-style: italic;
}
"""

# Interface with Suggestions
iface = gr.Interface(
    fn=gradio_search,
    inputs=[
        gr.Textbox(label="Enter your query", placeholder="e.g., machine learning, data science", lines=1, interactive=True),
        gr.Dropdown(choices=example_suggestions, label="Suggestions (Optional)", value=None),
    ],
    outputs=gr.HTML(label="Search Results"),
    title="Analytics Vidhya Smart Search",
    description="Find the most relevant courses from Analytics Vidhya based on your query.",
    theme="huggingface",
    css=custom_css,
)

if __name__ == "__main__":
    iface.launch()
