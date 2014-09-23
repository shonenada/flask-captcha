from .view import captcha_bp


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

        self.register_blueprint()

    def register_blueprint(self):
        self.app.register_blueprint(captcha_bp)
