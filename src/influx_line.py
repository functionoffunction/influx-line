class InfluxLineBuilder():
    """Influx line protocol builder.

    InfluxLineBuilder allow step by step building of valid Influx line protocol.

    Typical usage example:

    line = InfluxLineBuilder("weather")
    line.add_tag("location", "CA")
    line.add_field("temperature", 82.1)
    """

    # TODO: Add validation to __str__
    # TODO: Check for field, tags uniqueness
    # TODO: test out optional parts
    # TODO: add Docstrings
    # TODO: CI/CD to pypi

    def __init__(self, measure):
        self._measure = measure

    _tags = ""
    _fields = ""
    _timestamp = ""

    def set_measure(self, measure):
        """Sets measure name.

        Set measure name for the InfluxLineBuilder object. Calling it
        subsequently overwrite the measure valu

        Args:
        table_handle:
            An open smalltable.Table instance.

        Returns:
        None
        """
        self._measure = measure

    def set_timestamp(self, timestamp):
        self._timestamp = timestamp

    def add_tag(self, name, value):
        self._tags = self._tags + f",{name}={str(value)}"

    def add_field(self, name, value, is_integer: bool = False):
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
            self._fields = self._fields+f'{name}="{value}"'

    def _create_tag_fragment(self, name, value):
        tag_fragment = f"{name}={str(value)}"
        return tag_fragment

    def __str__(self):
        return f"{self._measure}"\
            f"{self._tags}" \
            " " \
            f"{self._fields}" \
            f"{'' if self._timestamp == '' else ' '+str(self._timestamp)}"
