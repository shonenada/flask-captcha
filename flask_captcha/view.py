import random
try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

from flask import Blueprint, send_file, make_response
from wheezy.captcha.image import captcha
from wheezy.captcha.image import background
from wheezy.captcha.image import curve
from wheezy.captcha.image import noise
from wheezy.captcha.image import smooth
from wheezy.captcha.image import text
from wheezy.captcha.image import offset
from wheezy.captcha.image import rotate
from wheezy.captcha.image import warp


captcha_bp = Blueprint('captcha', __name__)


@captcha_bp.route('/captcha')
def captcha_view():
    out = StringIO()
    capthca_image = captcha(drawings=[
        background(),
        text(fonts=['/home/vagrant/fonts/Tahoma-Bold.ttf'],
             drawings=[warp(), rotate(), offset()]),
        curve(),
        noise(),
        smooth(),
    ])
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    chars = random.sample(characters, 5)
    imgfile = capthca_image(''.join(chars))
    imgfile.save(out, 'PNG')
    out.seek(0)
    response = make_response(out.read())
    response.content_type = 'image/png'
    return response
