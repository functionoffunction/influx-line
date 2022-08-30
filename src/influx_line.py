class InfluxLine():
    """Influx line protocol builder.

    InfluxLine allow step by step building of valid Influx line protocol.

    Typical usage example:

    line = InfluxLine("weather")
    line.add_tag("location", "CA")
    line.add_field("temperature", 82.1)
    """

    def __init__(self, measure):
        self._measure = measure

    _tags = ""
    _fields = ""
    _timestamp = ""

    _escape_list = [" ", ",", "=", '"']

    def _escape(self, value):
        for char in self._escape_list:
            value = value.replace(char, f'\{char}')
        return value

    def set_measure(self, measure):
        """Sets measurement name.

        Set measure name for the InfluxLine object. Calling it
        subsequently overwrite the measure value

        Args:
        measure:
            the name of the measurement.

        Returns:
        None
        """
        self._measure = self._escape(measure)

    def set_timestamp(self, timestamp):
        """Sets timestamp.

        Set timestamp value for the InfluxLine object. Calling it
        subsequently overwrite the measure value

        Args:
        timestamp:
            the value of the measurement in nanoseconds

        Returns:
        None
        """
        self._timestamp = timestamp

    def add_tag(self, name, value):
        """add a tag to influx line.

        Adds a name and value of tag for the InfluxLine object.

        Args:
        name:
            the name of the tag

        value:
            the value of the tag

        Returns:
        None
        """
        self._tags = self._tags + \
            f",{self._escape(name)}={self._escape(str(value))}"

    def add_field(self, name, value, is_integer: bool = False):
        """add a field to influx line.

        Adds a name and value of field for the InfluxLine object.

        Args:
        name:
            the name of the field

        value:
            the value of the field

        Returns:
        None
        """
        if self._fields != "":
            self._fields = f"{self._fields},"
        if value is None:
            is_integer = False
            value = ''

        if isinstance(value, int) or isinstance(value, float):
            if is_integer:
                tag_fragment = self._create_tag_fragment(name, int(value))
                self._fields = self._fields+f"{tag_fragment}i"
            else:
                tag_fragment = self._create_tag_fragment(name, value)
                self._fields = self._fields+tag_fragment
        else:
            self._fields = self._fields + \
                f'{self._escape(name)}="{self._escape(value)}"'

    def _create_tag_fragment(self, name, value):
        tag_fragment = f"{self._escape(name)}={str(value)}"
        return tag_fragment

    def __str__(self):
        return f"{self._measure}"\
            f"{self._tags}" \
            " " \
            f"{self._fields}" \
            f"{'' if self._timestamp == '' else ' '+str(self._timestamp)}"
