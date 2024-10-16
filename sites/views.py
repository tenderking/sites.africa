# ./sites/views.py
from sites import app
from flask import render_template


@app.route("/")
def index():
    sites = [
        {"name": "site name 1", "url": "#", "category": "category 1"},
        {"name": "site name 2", "url": "#", "category": "category 1"},
        {"name": "site name 3", "url": "#", "category": "category 1"},
        {"name": "site name 4", "url": "#", "category": "category 1"},
        {"name": "site name 5", "url": "#", "category": "category 2"},
        {"name": "site name 6", "url": "#", "category": "category 2"},
        {"name": "site name 7", "url": "#", "category": "category 2"},
        {"name": "site name 8", "url": "#", "category": "category 2"},
    ]

    # Extract unique categories
    categories = list({site["category"] for site in sites})

    return render_template("index.html", categories=categories, sites=sites)
