from flask import Flask, redirect
from android.permissions import Permission, request_permissions

request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('https://www.pinterest.com')


if __name__ == "__main__":
    app.run(debug=False, port=8080)
