class SystemAnnouncement:

    def parse(self, json):
        self.announcement = json.get('announcement')
        self.message_begin_at = json.get('message_begin_at')
        self.message_expire_at = json.get('_message_expire_at')
        self.announcement_type = json.get('announcement_type')
        self.status = json.get('status')
        self.outage_time_start = json.get('outage_time_start')
        self.outage_time_end = json.get('outage_time_end')

    @property
    def announcement(self):
        return self._announcement

    @property
    def message_begin_at(self):
        return self._message_begin_at

    @property
    def message_expire_at(self):
        return self._message_expire_at

    @property
    def announcement_type(self):
        return self._announcement_type

    @property
    def status(self):
        return self._status

    @property
    def outage_time_start(self):
        return self._outage_time_start

    @property
    def outage_time_end(self):
        return self._outage_time_end
