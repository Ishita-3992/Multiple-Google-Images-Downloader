from google_images_search import GoogleImagesSearch
import os

def search_and_download_images(keyword, num_images):
    # Initialize GoogleImagesSearch
    gis = GoogleImagesSearch('AIzaSyBA9l0PQCa-aSV6M4w6okAjVV5g32aBXxA', '27ebef0472a294dd8')

    # Define search parameters
    search_params = {
        'q': keyword,
        'num': num_images,
        'safe': 'high',  # High safety level
    }

    # Path to save downloaded images
    path_to_images = './static/images/'

    # Create directory if it doesn't exist
    if not os.path.exists(path_to_images):
        os.makedirs(path_to_images)

    # Clear any existing images in the folder
    for f in os.listdir(path_to_images):
        os.remove(os.path.join(path_to_images, f))

    try:
        # Execute search and download
        gis.search(search_params=search_params, path_to_dir=path_to_images)
        return f'{num_images} images of "{keyword}" downloaded to {path_to_images}'
    except Exception as e:
        return f'An error occurred: {e}'