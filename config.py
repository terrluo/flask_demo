class BaseConfig:
    ENV = "development"


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    ENV = "production"
    DEBUG = False


config_map = {
    "dev": DevConfig,
    "prod": ProdConfig,
}