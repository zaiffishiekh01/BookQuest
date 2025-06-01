from flask import Flask,render_template,request, flash, redirect, url_for
import pickle
import numpy as np
import os
from dotenv import load_dotenv
import requests
from io import BytesIO

# Load environment variables
load_dotenv()

# Use /tmp directory for file storage
DATA_DIR = '/tmp/bookquest_data'
os.makedirs(DATA_DIR, exist_ok=True)

def load_pickle_from_url(url, local_filename):
    local_path = os.path.join(DATA_DIR, local_filename)
    if os.path.exists(local_path):
        with open(local_path, 'rb') as f:
            return pickle.load(f)
    response = requests.get(url)
    response.raise_for_status()
    with open(local_path, 'wb') as f:
        f.write(response.content)
    return pickle.load(BytesIO(response.content))

POPULAR_URL = "https://huggingface.co/zaiffi/BookQuest/resolve/main/popular.pkl"
PT_URL = "https://huggingface.co/zaiffi/BookQuest/resolve/main/pt.pkl"
BOOKS_URL = "https://huggingface.co/zaiffi/BookQuest/resolve/main/books.pkl"
SIMILARITY_URL = "https://huggingface.co/zaiffi/BookQuest/resolve/main/similarity_scores.pkl"

popular_df = load_pickle_from_url(POPULAR_URL, "popular.pkl")
pt = load_pickle_from_url(PT_URL, "pt.pkl")
books = load_pickle_from_url(BOOKS_URL, "books.pkl")
similarity_scores = load_pickle_from_url(SIMILARITY_URL, "similarity_scores.pkl")

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# EmailJS Configuration
app.config['EMAILJS_PUBLIC_KEY'] = os.getenv('VITE_EMAILJS_PUBLIC_KEY')
app.config['EMAILJS_SERVICE_ID'] = os.getenv('VITE_EMAILJS_SERVICE_ID')
app.config['EMAILJS_TEMPLATE_ID'] = os.getenv('VITE_EMAILJS_TEMPLATE_ID')

@app.route("/")
def index():
    return render_template('index.html',
                           ISBN = list(popular_df['ISBN'].values),
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           release_year = list(popular_df['Year-Of-Publication'].values),
                           publisher = list(popular_df['Publisher'].values),
                           image = list(popular_df['Image-URL-M'].values),
                           votes = list(popular_df['num_ratings'].values),
                           rating = list(popular_df['avg_rating'].values)
                           )

@app.route("/recommend")
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    try:
        # fetching index
        index = np.where(pt.index == user_input)[0][0]
    except IndexError:
        # Book not found, show a friendly error
        return render_template('recommend.html', error=f'No recommendations found for "{user_input}". Please try another book title.')

    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:11]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['ISBN'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Year-Of-Publication'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Publisher'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    return render_template('recommend.html', data=data, user_input=user_input)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would typically handle the form submission
        # For example, sending an email or storing in a database
        # For now, we'll just show a success message
        
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
