class ServerGroup:

    def parse(self, json):
        self.id = json.get('id')
        self.name = json.get('name')
        self.tag = json.get('tag')
        self.policy_ids = json.get('policy_ids')
        self.windows_policy_ids = json.get('windows_policy_ids')
        self.fim_policy_ids = json.get('fim_policy_ids')
        self.linux_fim_policy_ids = json.get('linux_fim_policy_ids')
        self.windows_fim_policy_ids = json.get('windows_fim_policy_ids')
        self.lids_policy_ids = json.get('lids_policy_ids')
        self.linux_firewall_policy_id = json.get('linux_firewall_policy_id')
        self.windows_firewall_policy_id = json.get(
            'windows_firewall_policy_id')
        self.firewall_policy_id = json.get('firewall_policy_id')
        self.special_events_policy_id = json.get('special_events_policy_id')
        self.alert_profile_id = json.get('alert_profile_id')

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def tag(self):
        return self._tag

    @property
    def policy_ids(self):
        return self._policy_ids

    @property
    def windows_policy_ids(self):
        return self._windows_policy_ids

    @property
    def fim_policy_ids(self):
        return self._fim_policy_ids

    @property
    def linux_fim_policy_ids(self):
        return self._linux_fim_policy_ids

    @property
    def windows_fim_policy_ids(self):
        return self._windows_fim_policy_ids

    @property
    def lids_policy_ids(self):
        return self._lids_policy_ids

    @property
    def linux_firewall_policy_id(self):
        return self._linux_firewall_policy_id

    @property
    def windows_firewall_policy_id(self):
        return self._windows_firewall_policy_id

    @property
    def firewall_policy_id(self):
        return self._firewall_policy_id

    @property
    def special_events_policy_id(self):
        return self._special_events_policy_id

    @property
    def alert_profile_id(self):
        return self._alert_profile_id
