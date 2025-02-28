

class OpenSearchConnectionConfig:
        
    def __init__(
        self, 
        hosts: any, 
        auth: any,
        http_compress: bool = True, 
        use_ssl: bool = False,
        verify_certs: bool = False,
        ssl_assert_hostname: bool = False,
        ssl_show_warn: bool = False
    ) -> None:
        self.hosts = hosts
        self.auth = auth
        self.http_compress = http_compress
        self.use_ssl = use_ssl
        self.verify_certs = verify_certs
        self.ssl_assert_hostname = ssl_assert_hostname
        self.ssl_show_warn = ssl_show_warn
