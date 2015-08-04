class Server:

    def parse(self, json):
        self.id = json.get('id')
        self.url = json.get('url')
        self.hostname = json.get('hostname')
        self.server_label = json.get('server_label')
        self.reported_fqdn = json.get('reported_fqdn')
        self.connecting_ip_address = json.get('connecting_ip_address')
        self.state = json.get('state')
        self.daemon_version = json.get('daemon_version')
        self.read_only = json.get('read_only')
        self.platform = json.get('platform')
        self.platform_version = json.get('platform_version')
        self.os_version = json.get('os_version')
        self.kernel_name = json.get('kernel_name')
        self.kernel_machine = json.get('kernel_machine')
        self.self_verification_failed = json.get('self_verification_failed')
        self.connecting_ip_fqdn = json.get('connecting_ip_fqdn')
        self.group_id = json.get('group_id')
        self.group_name = json.get('group_name')
        self.proxy = json.get('proxy')
        self.interfaces = json.get('interfaces')
        self.firewall_policy = json.get('firewall_policy')

    @property
    def id(self):
        """Identifier for this server."""
        return self._id

    @property
    def url(self):
        return self._url

    @property
    def hostname(self):
        return self._hostname

    @property
    def server_label(self):
        return self._server_label

    @property
    def reported_fqdn(self):
        return self._reported_fqdn

    @property
    def connecting_ip_address(self):
        return self._connecting_ip_address

    @property
    def state(self):
        return self._state

    @property
    def daemon_version(self):
        return self._daemon_version

    @property
    def read_only(self):
        return self._read_only

    @property
    def platform(self):
        return self._platform

    @property
    def platform_version(self):
        return self._platform_version

    @property
    def os_version(self):
        return self._os_version

    @property
    def kernel_name(self):
        return self._kernel_name

    @property
    def kernel_machine(self):
        return self._kernel_machine

    @property
    def self_verification_failed(self):
        return self._self_verification_failed

    @property
    def connecting_ip_fqdn(self):
        return self._connecting_ip_fqdn

    @property
    def group_id(self):
        return self._group_id

    @property
    def group_name(self):
        return self._group_name

    @property
    def proxy(self):
        return self._proxy

    @property
    def interfaces(self):
        return self._interfaces

    @property
    def firewall_policy(self):
        return self._firewall_policy
