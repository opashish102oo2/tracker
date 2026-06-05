import cloudinary
import cloudinary.uploader
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Cloudinary Configuration
cloudinary.config(
    cloud_name="dqsetcecu",
    api_key="119182683135652",
    api_secret="9Qbv-lCwg7oN_dkDtjHESAbhLIw"
)

UPLOAD_FOLDER = "photos"

# Photos folder automatically create karega
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Location Save
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["photo"]

    result = cloudinary.uploader.upload(file)

    print("\n========== PHOTO UPLOADED ==========")

    print("Image URL:")
    print(result["secure_url"])

    return {
        "status": "uploaded",
        "url": result["secure_url"]
    }

# Run Server
if __name__ == "__main__":
    app.run(debug=True)