from dotenv import load_dotenv

load_dotenv()

def create_app(config_name=None):
    import os

    from flask import Flask

    from config import config_map

    if not config_name:
        config_name = os.getenv("DEMO_ENV")

    config_object = config_map.get(config_name)
    if not config_object:
        raise SystemExit("config 不存在，启动 flask 失败")

    app = Flask(__name__)
    app.config.from_object(config_object)

    return app
