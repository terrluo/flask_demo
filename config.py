class BaseConfig:
    ENV = "development"


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


config_map = {
    "dev": DevConfig,
    "prod": ProdConfig,
}