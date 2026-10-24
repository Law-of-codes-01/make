import os
import secrets
from flask import current_app
import secrets
import cloudinary
import cloudinary.uploader



cloudinary.config(
    cloud_name=os.environ.get("cloud_id"),
    api_key=os.environ.get("cloud_Api_key"),
    api_secret=os.environ.get("cloud_Api_secret"),
    secure=True
)

def save_med(s_pic):
    result = cloudinary.uploader.upload(
        s_pic,
        public_id=secrets.token_hex(8),
        folder="post_file",
        resource_type="auto",
    )
    return result["secure_url"]
