from opensearchpy import OpenSearch

from data.opensearch.opensearch_connection_config import OpenSearchConnectionConfig

from config import settings

class OpenSearchClientWrapper:

    def __init__(
        self, 
        connection_config: OpenSearchConnectionConfig
     ) -> None:
        self.connection_config = connection_config
        self.client = None

    def open(self) -> None:
        try:
            self.client = OpenSearch(
                hosts = self.connection_config.hosts,
                http_auth = self.connection_config.auth, 
                http_compress = self.connection_config.http_compress, # enables gzip compression for request bodies
                use_ssl = self.connection_config.use_ssl,
                verify_certs = self.connection_config.verify_certs,
                ssl_assert_hostname = self.connection_config.ssl_assert_hostname,
                ssl_show_warn = self.connection_config.ssl_show_warn
            )
        except Exception as e:
            self.client = None
            raise Exception(f"Error while trying to open OpenSearch client: {e}")

    def close_quietly(self) -> None:
        if self.isclosed():
            return
        try:
            self.client.close()
        finally:
            self.client = None

    def reopen(self) -> None:
        self.close_quietly()
        self.open()

    def isclosed(self) -> bool:
        return self.client is None
    
    def execute_query(
        self, 
        query: dict,
        index: str
    ) -> list:
        if self.isclosed():
            raise Exception(f"OpenSearch client not initialized yet!")
        response = self.client.search(
            body = query,
            index = index
        )
        return response["hits"]["hits"]
    
opensearch_client_wrapper = OpenSearchClientWrapper(
    connection_config=OpenSearchConnectionConfig(
        hosts=[settings.OPENSEARCH_URL],
        auth=(settings.OPENSEARCH_USR, settings.OPENSEARCH_PSW)
    )
)