from .view import captcha_bp
from flask import session


CHARS = 'aabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class _CaptchaExtension(object):

    def __init__(self, captcha, app):
        self.captcha = captcha
        self.app = app


class Captcha(object):

    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app)
        else:
            self.app = None

    def init_app(self, app):
        self.app = app

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['captcha'] = _CaptchaExtension(self, app)

        app.config.setdefault('CAPTCHA_CHARACTERS', CHARS)
        app.config.setdefault('CAPTCHA_CHARS_LENGTH', 4)
        app.config.setdefault('CAPTCHA_FONTS', [])
        app.config.setdefault('CAPTCHA_CASE_SENSITIVE', False)

        self.register_blueprint()
    
    def validate(self, code):
        if self.app.config['CAPTCHA_CASE_SENSITIVE']:
            return code == session['captcha']
        else:
            return code.lower() == session['captcha'].lower()

    def register_blueprint(self):
        self.app.register_blueprint(captcha_bp)
