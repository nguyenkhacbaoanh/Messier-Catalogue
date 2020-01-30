"""Application Configuration."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config(object):
    """Parent configuration class."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    TITLE = "Flask API"
    VERSION = "0.1.0"
    DESCRIPTION = "An API with galaxy catalogs."


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}/catalogue-database-dev.db".format(basedir)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Configurations for Testing."""

    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///{}/catalogue-database-test.db".format(basedir)
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///{}/catalogue-database-prod.db".format(basedir)


config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}