import requests

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://localhost:8170/JackLinJQL/image-translator/")

# Print the status code of the response.
def imageTranslate():
    return(response.content)

imageTranslate()
