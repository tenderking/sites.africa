# ./sites/__init__.py
from flask import Flask

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

from sites import views  # Import views after app is created
