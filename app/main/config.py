"""Application Configuration."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Parent configuration class."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    TITLE = "Flask API"
    VERSION = "0.1.0"
    DESCRIPTION = "An API with galaxy catalogs."
    SWAGGER_UI_DOC_EXPANSION = 'list'


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/catalogue-database-dev.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Configurations for Testing."""

    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/catalogue-database-test.db"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/catalogue-database-prod.db"


config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}
