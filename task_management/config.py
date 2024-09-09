from pydantic_settings import BaseSettings


class ElasticSearchConfig(BaseSettings):
    HOST: str = "http://localhost/"
    PORT: int = 9200
    CONNECTION_POOL_SIZE: int = 10
    RETRY_ON_TIMEOUT: bool = False
    SNIFF_ON_START: bool = False
    SNIFF_ON_CONNECTION_FAIL: bool = False
    PATH_TO_QUERY_TEMPLATE: str = "./task_management/repository/es_templates"
    INDEX_NAME: str = "task_details"
    

ES_CONFIG = ElasticSearchConfig()
