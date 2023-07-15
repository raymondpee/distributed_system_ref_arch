from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Route to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Route to create a new book
@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if data and "title" in data and "author" in data:
        new_book = {
            "id": len(books) + 1,
            "title": data["title"],
            "author": data["author"]
        }
        books.append(new_book)
        return jsonify(new_book), 201
    else:
        return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
