import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuoteHub.settings")

import django
django.setup()

from quotes.models import Quote

quotes_data = [
    {
        "quote": "Believe you can and you're halfway there.",
        "author": "Theodore Roosevelt",
    },
    {
        "quote": "It always seems impossible until it's done.",
        "author": "Nelson Mandela",
    },
    {
        "quote": "Stay hungry, stay foolish.",
        "author": "Steve Jobs",
    },
    
    {
        "quote": "The future depends on what you do today.",
        "author": "Mahatma Gandhi",
    },
    {
        "quote": "Great things are done by a series of small things brought together.",
        "author": "Vincent van Gogh",
    },
    {
        "quote": "Dream big and dare to fail.",
        "author": "Norman Vaughan",
    },
    {
        "quote": "Do what you can, with what you have, where you are.",
        "author": "Theodore Roosevelt",
    },
    {
        "quote": "Believe in yourself and all that you are.",
        "author": "Christian D. Larson",
    },
    {
        "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "author": "Winston Churchill",
    },
    {
        "quote": "It does not matter how slowly you go as long as you do not stop.",
        "author": "Confucius",
    },
    {
        "quote": "Act as if what you do makes a difference. It does.",
        "author": "William James",
    },
    {
        "quote": "The secret of getting ahead is getting started.",
        "author": "Mark Twain",
    },
    {
        "quote": "Everything you can imagine is real.",
        "author": "Pablo Picasso",
    },
    {
        "quote": "Happiness depends upon ourselves.",
        "author": "Aristotle",
    },
    {
        "quote": "Turn your wounds into wisdom.",
        "author": "Oprah Winfrey",
    },
    {
        "quote": "You miss 100% of the shots you don't take.",
        "author": "Wayne Gretzky",
    },
    {
        "quote": "Nothing will work unless you do.",
        "author": "Maya Angelou",
    },
    {
        "quote": "Difficulties in life are intended to make us better, not bitter.",
        "author": "Dan Reeves",
    },
    {
        "quote": "If opportunity doesn't knock, build a door.",
        "author": "Milton Berle",
    },
    {
        "quote": "Every moment is a fresh beginning.",
        "author": "T. S. Eliot",
    },
    {
        "quote": "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "author": "Walt Whitman",
    },
    {
        "quote": "You are never too old to set another goal or to dream a new dream.",
        "author": "C. S. Lewis",
    },
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
    },
    {
        "quote": "Small deeds done are better than great deeds planned.",
        "author": "Peter Marshall",
    },
    {
        "quote": "Be yourself; everyone else is already taken.",
        "author": "Oscar Wilde",
    },
    {
        "quote": "No pressure, no diamonds.",
        "author": "Thomas Carlyle",
    },
    {
        "quote": "What we think, we become.",
        "author": "Buddha",
    },
    {
        "quote": "Believe you deserve it and the universe will serve it.",
        "author": "Unknown",
    },
    {
        "quote": "One day or day one. You decide.",
        "author": "Unknown",
    },
    {
        "quote": "Make yourself a priority.",
        "author": "Unknown",
    },
    {
        "quote": "Your only limit is your mind.",
        "author": "Unknown",
    },
    {
        "quote": "Progress, not perfection.",
        "author": "Unknown",
    },
    {
        "quote": "Be stronger than your excuses.",
        "author": "Unknown",
    },
]

for item in quotes_data:
    Quote.objects.get_or_create(
        quote=item["quote"],
        defaults={"author": item["author"]},
    )

print("Quotes added successfully!")