import threading
import requests

# ✅ Step 1: List of file URLs (replace with real image/pdf links)
file_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg",
    "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4",
    "https://file-examples.com/wp-content/uploads/2017/10/file_example_PDF_1MB.pdf"
]

# ✅ Step 2: Define the function to download a file
def download_file(url, file_number):
    response = requests.get(url)
    file_name = f"file_{file_number}.jpg"
    with open(file_name, "wb") as file:
        file.write(response.content)
    print(f"✅ Downloaded: {file_name}")

# ✅ Step 3: Create and start a thread for each file
threads = []

for index, url in enumerate(file_urls):
    thread = threading.Thread(target=download_file, args=(url, index + 1))
    thread.start()
    threads.append(thread)

# ✅ Step 4: Wait for all threads to finish
for thread in threads:
    thread.join()

print("All downloads completed.")




