import os
import orjson

import urllib3
from jinja2 import Environment, FileSystemLoader


from elasticsearch import Elasticsearch
from elasticsearch.connection import Urllib3HttpConnection


class ElasticRepository:
    def __init__(self, es_config, es_connection=None):
        self.es = (
            Elasticsearch(
                es_config.HOST,
                port=es_config.PORT,
                maxsize=es_config.CONNECTION_POOL_SIZE,
                retry_on_timeout=es_config.RETRY_ON_TIMEOUT,
                sniff_on_start=es_config.SNIFF_ON_START,
                sniff_on_connection_fail=es_config.SNIFF_ON_CONNECTION_FAIL,
                connection_class=Urllib3HttpConnection,
                headers=urllib3.make_headers(
                    keep_alive=True, accept_encoding=True),
            )
            if es_connection is None
            else es_connection
        )
        self.query_templates = {}

    def _build_template(self, data_dir):
        jinja_env = Environment(loader=FileSystemLoader(data_dir))
        jinja_env.filters["jsonify"] = orjson.dumps
        for template_json in os.listdir(data_dir):
            self.query_templates[template_json.split(".")[0]] = jinja_env.get_template(
                template_json
            )
