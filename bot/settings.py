from pydantic_settings import BaseSettings

from dotenv import load_dotenv

import os, json

from yarl import URL



load_dotenv()


class Settings(BaseSettings):

    BOT_TOKEN: str = os.getenv("BOT_TOKEN").strip()

    FSM_REDIS_HOST: str = os.getenv("FSM_REDIS_HOST").strip()
    FSM_REDIS_DB: int = os.getenv("FSM_REDIS_DB").strip()

    REDIS_HOST: str = os.getenv("REDIS_HOST").strip()
    REDIS_DB: int = os.getenv("REDIS_DB").strip()

    # Путь к логам
    PATH_LOGS: str = "bot/data/logs.log"

    ADMIN_IDS: list[int] = json.loads(os.getenv("ADMIN_IDS"))

    FRUITS: dict = {
        "🍌": "fruit_1",
        "🍏": "fruit_2",
        "🍎": "fruit_3",
        "🍒": "fruit_4",
        "🍓": "fruit_5",
        "🍑": "fruit_6"
    }

    @property
    def fsm_redis_url(self) -> str:
        """
        создание URL для подключения к редису

        :return: redis connection url
        """
        return str(URL.build(
            scheme="redis",
            host=self.FSM_REDIS_HOST,
            path="/" + str(self.FSM_REDIS_DB)
        ))


settings = Settings()
