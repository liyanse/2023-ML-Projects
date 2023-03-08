class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'jhfduhfd8754827ywehujkfh977428T%^#@#TYHGF55t7yhlgjhhsddfda'
    OPENAI_KEY =  "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"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
   


