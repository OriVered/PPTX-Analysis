# File: main.py
import os
import time

from client import PPTXAnalysisClient

CURRENT_DIR = os.getcwd()
DIRECTORY_PATH = os.path.dirname(os.path.dirname(CURRENT_DIR))
FILE_PATH = os.path.join(DIRECTORY_PATH, 'presentation.pptx')

def main():
    # Create an instance of the client
    client = PPTXAnalysisClient("http://localhost:5000")

    # Upload a file
    filepath = FILE_PATH
    uid = client.upload(filepath)
    print(f"Uploaded file with UID: {uid}")

    # Check the status of the upload
    status = client.status(uid)
    print(f"Status: {status.status}")
    print(f"Filename: {status.filename}")
    print(f"Timestamp: {status.timestamp}")

    time.sleep(100)
    # Check the status of the upload
    status = client.status(uid)
    print(f"Status: {status.status}")
    print(f"Filename: {status.filename}")
    print(f"Timestamp: {status.timestamp}")

    # Check if the processing is done
    if status.is_done():
        print("Processing is done")
    else:
        print("Processing is still ongoing")

if __name__ == "__main__":
    main()
