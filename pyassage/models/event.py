class Event:
    """
        A data object for the CloudPassage event type documented here:

        https://support.cloudpassage.com/entries/23125117-Events#event-types
    """
    def __str__(self):
        return '{0}: {1}'.format(self.created_at, self.type)

    def parse(self, json):
        self.id = json.get('id')
        self.type = json.get('type')
        self.name = json.get('name')
        self.critical = json.get('critical')
        self.created_at = json.get('created_at')
        self.message = json.get('message')
        self.policy_name = json.get('policy_name')
        self.original_log_entry = json.get('original_log_entry')
        self.target_username = json.get('target_username')
        self.object_name = json.get('object_name')
        self.cpe = json.get('cpe')

        self.api_key_id = json.get('api_key_id')
        self.api_key_label = json.get('api_key_label')

        self.package_name = json.get('package_name')
        self.package_version = json.get('package_version')

        self.daemon_version = json.get('daemon_version')
        self.previous_daemon_version = json.get('previous_daemon_version')

        self.server_hostname = json.get('server_hostname')
        self.server_ip_address = json.get('server_ip_address')
        self.server_reported_fqdn = json.get('server_reported_fqdn')
        self.server_label = json.get('server_label')
        self.server_display_name = json.get('server_display_name')
        self.server_primary_ip_address = json.get('server_primary_ip_address')
        self.server_id = json.get('server_id')
        self.server_platform = json.get('server_platform')
        self.server_group_name = json.get('server_group_name')
        self.server_new_ip_address = json.get('server_new_ip_address')
        self.server_old_ip_address = json.get('server_old_ip_address')
        self.server_account_username = json.get('server_account_username')
        self.server_account_id = json.get('server_account_id')

        self.actor_key_id = json.get('actor_key_id')
        self.actor_key_label = json.get('actor_key_label')
        self.actor_username = json.get('actor_username')
        self.actor_ip_address = json.get('actor_ip_address')
        self.actor_country = json.get('actor_country')

        self.rule_name = json.get('rule_name')
        self.rule_reference_identifiers = \
            json.get('rule_reference_identifiers')

        self.cves = json.get('cves')

    @property
    def id(self):
        """Identifier for this event."""
        return self._id

    @property
    def type(self):
        """The name of the event type, as used by the CloudPassage API."""
        return self._type

    @property
    def name(self):
        """The name of the event, as displayed in the Halo Portal."""
        return self._name

    @property
    def critical(self):
        """Boolean critical value"""
        return self._critical

    @property
    def created_at(self):
        """Event creation timestamp. Formatted in ISO 8601."""
        return self._created_at

    @property
    def message(self):
        """message  Event's message."""
        return self.message

    @property
    def policy_name(self):
        """Name of the policy that triggered the event."""
        return self._policy_name

    @property
    def server_hostname(self):
        """Name of the policy that triggered the event."""
        return self._server_hostname

    @property
    def server_ip_address(self):
        """Server's connecting IP address."""
        return self._server_ip_address

    @property
    def server_reported_fqdn(self):
        return self._server_reported_fqdn

    @property
    def server_label(self):
        """A user-assigned label or description for the server."""
        return self._server_label

    @property
    def server_display_name(self):
        """
            (In priority order) either server_label, server_reported_fqdn,
            or server_hostname.
        """
        return self._server_display_name

    @property
    def server_primary_ip_address(self):
        return self._server_primary_ip_address

    @property
    def server_id(self):
        """Server's unique ID"""
        return self._server_id

    @property
    def server_platform(self):
        return self._server_platform

    @property
    def server_group_name(self):
        """Server's group name."""
        return self._server_group_name

    @property
    def original_log_entry(self):
        """
            The full text of the triggering log entry (for LIDS events). May
            be empty, or plain text, XML, or other format.
        """
        return self._original_log_entry

    @property
    def server_new_ip_address(self):
        """xxx"""
        return self._server_new_ip_address

    @property
    def x(self):
        """Server's new IP address. (For address-change events.)"""
        return self._x

    @property
    def server_old_ip_address(self):
        """Server's old IP addres. (For address-change events.)"""
        return self._server_old_ip_address

    @property
    def actor_key_id(self):
        """
            The ID of the API key used. (For key-related events that have
            an actor.)
        """
        return self._actor_key_id

    @property
    def actor_key_label(self):
        """
            The label of the API key used. (For key-related events that have
            an actor.)
        """
        return self._actor_key_label

    @property
    def actor_username(self):
        """
            Username of the user who requested the change. (For events that
            have an actor.)
        """
        return self._actor_username

    @property
    def actor_ip_address(self):
        """
            IP address of the user who requested the change. (For events
            that have an actor.)
        """
        return self._actor_ip_address

    @property
    def actor_country(self):
        """
            Location of the user who requested the change. (For events that
            have an actor.)
        """
        return self._actor_country

    @property
    def target_username(self):
        """
            Username of the user that is being modified. (For account-related
            events.)
        """
        return self._target_username

    @property
    def daemon_version(self):
        """Current version of the Halo agent. (For agent-related events.)"""
        return self._daemon_version

    @property
    def previous_daemon_version(self):
        """
            Previous version of the Halo agent. (For agent version-change
            events.)
        """
        return self._previous_daemon_version

    @property
    def rule_name(self):
        """
            Configuration or log-based intrusion detection policy rule
            that failed.
        """
        return self._rule_name

    @property
    def rule_reference_identifiers(self):
        """
            An optional comma-separated list of IDs applied to this policy
            rule for compliance purposes.
        """
        return self._rule_reference_identifiers

    @property
    def server_account_username(self):
        """Local server account username. (For account-related events.)"""
        return self._server_account_username

    @property
    def server_account_id(self):
        """Local server account id. (For account-related events.)"""
        return self._server_account_id

    @property
    def object_name(self):
        """
            Name of the FIM object. For a file it is a file path.
            (For FIM events.)
        """
        return self._object_name

    @property
    def api_key_id(self):
        """API Key's ID. (For key-related events.)"""
        return self._api_key_id

    @property
    def api_key_label(self):
        """API Key's name. (For key-related events.)"""
        return self._api_key_label

    @property
    def package_name(self):
        """The name of the software package in this (vulnerability) event."""
        return self._package_name

    @property
    def package_version(self):
        """
            The version number of the software package in this
            (vulnerability) event.
        """
        return self._package_version

    @property
    def cves(self):
        """
            An array of the CVEs in this (vulnerability) event. Each CVE
            has the following subfields:

            - CVE   The Common Vulnerability and Exposure identifier
                    for this CVE.
            - CVSS  The Common Vulnerability Scoring System (CVSS)
                    score for the severity of this CVE.
        """
        return self._cves

    @property
    def cpe(self):
        """
            (Windows) The Common Platform Enumeration (CPE) name for the
            package in this (vulnerability) event.
        """
        return self._cpe
