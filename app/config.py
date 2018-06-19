import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv('SECRET') or "secret"



class DevelopmentConfiguration(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfiguration(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True


class ProductionConfiguration(Config):
    """Configurations for Production."""
    DEBUG = False

configuration = {
    'DEFAULT': DevelopmentConfiguration,
    'TESTING': TestingConfiguration,
    'DEVELOPMENT': DevelopmentConfiguration,
    'PRODUCTION': ProductionConfiguration
}
