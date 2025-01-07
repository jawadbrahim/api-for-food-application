from google.cloud import storage
from google.oauth2 import service_account

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    try:
        credentials = service_account.Credentials.from_service_account_file(
            'C:/Users/Jawad Ibrahim/Downloads/moonlit-sphinx-447015-s5-795cfec99d00.json')
        storage_client = storage.Client(credentials=credentials, project='moonlit-sphinx-447015-s5')
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_path)
        blob.make_public()
        return blob.public_url
    except Exception as e:
        raise Exception(f"Error uploading to GCS: {e}")

