---
title: BookQuest
emoji: 📚
colorFrom: blue
colorTo: yellow
sdk: docker
sdk_version: 3.1.1
app_file: app.py
pinned: false
---

# BookQuest: Adventure in Finding Great Reads

BookQuest is an intelligent book recommendation platform that helps you discover your next favorite read. Whether you're looking for classics, trending titles, or personalized suggestions, BookQuest makes finding great books effortless and enjoyable.

![Top 50 Books](public/Top_50_Books.png)

## Problem Statement

Finding the right book can be overwhelming with the sheer volume of options available. Readers often struggle to:
- Discover books tailored to their interests
- Get reliable recommendations
- Explore new genres and authors
- Connect with a modern, user-friendly interface

BookQuest solves these challenges by providing curated lists, smart recommendations, and a beautiful, intuitive experience.

## Features

- **Top 50 Books**: Instantly browse the most popular and highly rated books
- **Personalized Recommendations**: Get book suggestions based on your favorite titles
- **Modern UI**: Clean, responsive design with a focus on readability and ease of use
- **Contact Form**: Reach out for support or suggestions directly from the app
- **Live Search**: Quickly find books by title
- **Robust Backend**: Powered by Flask and machine learning models for accurate recommendations
- **Email Notifications**: Contact form uses EmailJS for instant communication

![Contact Us](public/contact_us(1).png)

## Tech Stack

- **Frontend & Application**: Flask, Bootstrap, HTML/CSS, Jinja2
- **Backend**: Python, Pandas, Numpy, Scikit-learn
- **Recommendation Engine**: Collaborative filtering using similarity scores
- **Email Integration**: EmailJS (client-side)
- **Deployment**: Docker, Hugging Face Spaces

## Getting Started

### Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- (Optional) Docker for containerized deployment

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zaiffishiekh01/BookQuest.git
   cd BookQuest
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file in the project root with your EmailJS credentials:**
   ```env
   SECRET_KEY=your-secret-key-here
   VITE_EMAILJS_PUBLIC_KEY=your-public-key-here
   VITE_EMAILJS_SERVICE_ID=your-service-id-here
   VITE_EMAILJS_TEMPLATE_ID=your-template-id-here
   ```

### Running the Application

Start the Flask app:
```bash
flask run --host=0.0.0.0 --port=7860
```

Or use Docker:
```bash
docker build -t bookquest .
docker run -p 7860:7860 bookquest
```

The application will be available at `http://localhost:7860`.

## Usage Guide

### Home Page (Top 50 Books)
- Browse the most popular books with cover images, authors, ratings, and more.
- Click on any book for more details.

![Top 50 Books](public/Top_50_Books.png)

### Recommendations
- Enter a book title you like and get a list of similar books instantly.
- Each recommendation includes cover, author, year, and publisher.

![Book Recommendations](public/Book_recommendations(1).png)
![Book Recommendations](public/Book_recommendations(2).png)

### Contact Us
- Use the contact form to send feedback or questions.
- EmailJS integration ensures your message is delivered instantly.

![Contact Us](public/contact_us(1).png)
![Contact Us](public/contact_us(2).png)

## Environment Variables

For security, do not share your actual `.env` file. Use this template:

```env
SECRET_KEY=your-secret-key-here
VITE_EMAILJS_PUBLIC_KEY=your-public-key-here
VITE_EMAILJS_SERVICE_ID=your-service-id-here
VITE_EMAILJS_TEMPLATE_ID=your-template-id-here
```

## Hugging Face Spaces Integration

When deploying on Hugging Face Spaces, use their Secret Management for your environment variables:
1. Go to your Space settings
2. Add each variable from your `.env` file as a secret
3. Hugging Face Spaces will make these available to your app

## Troubleshooting

- **Email Not Sending**: Check your EmailJS credentials and template IDs
- **Book Data Not Loading**: Ensure you have internet access to fetch remote model files
- **Docker Issues**: Make sure Docker is installed and running
- **UI Problems**: Clear your browser cache or try a different browser

## About the Developer

Developed by Muhammad Huzaifa Saqib (zaiffi), passionate about building AI-powered tools for readers and learners.

- GitHub: [zaiffishiekh01](https://github.com/zaiffishiekh01)
- LinkedIn: [Muhammad Huzaifa Saqib](https://www.linkedin.com/in/muhammad-huzaifa-saqib-90a1a9324/)
- Email: huzaifasaqib420@gmail.com

---

Enjoy your journey to great reads with **BookQuest**! 📚
