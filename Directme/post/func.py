import os

import secrets
from flask import current_app
def save_med(s_pic):
    rnd_hex=secrets.token_hex(8)
    _,pth=os.path.splitext(s_pic.filename)
    pic_nm=rnd_hex + pth
    if pth.lower() ==".mp4":
        pic_path=os.path.join(current_app.root_path,'static/videos',pic_nm)
    elif pth.lower() ==".mp3" or pth.lower() ==".m4a":
        pic_path=os.path.join(current_app.root_path,'static/audios',pic_nm)
    else:
        pic_path=os.path.join(current_app.root_path,'static/images',pic_nm)
    s_pic.save(pic_path)
    return pic_nm