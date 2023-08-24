import sys
import os
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_folder, ".."))

from myapi import app
if __name__ == '__main__':
    app = app
    app.run(debug=True)

