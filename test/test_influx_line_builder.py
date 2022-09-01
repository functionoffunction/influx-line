from unittest import TestCase
from src.influx_line import InfluxLine


class InfluxLineTestCase(TestCase):
    def setUp(self):
        self.measure = "weather"
        self.sample_time_stamp = "1465839830100400200"
        self.line_without_timestamp = self.complete_line = "weather,"\
            "location=us-midwest,season=summer" \
            " " \
            'temperature=82i,error=0.1,time_zone="CDT"'

        self.complete_line = self.line_without_timestamp + \
            " " \
            f"{self.sample_time_stamp}"

        self.line_with_none_field = "weather,"\
            "location=us-midwest,season=summer" \
            " " \
            'temperature="",error="",time_zone=""'

    def test_get_line_with_timestamp(self):
        """Test InfluxLine build produce right line,
         when containing timestamp """
        line = InfluxLine("weather")
        line.add_tag("location", "us-midwest")
        line.add_tag("season", "summer")
        line.add_field("temperature", 82, is_integer=True)
        line.add_field("error", 0.1)
        line.add_field("time_zone", "CDT")
        line.set_timestamp(self.sample_time_stamp)
        self.assertEqual(str(line), self.complete_line)

    def test_get_line_without_timestamp(self):
        """Test InfluxLine build produce right line,
         when containing not timestamp"""
        line = InfluxLine("weather")
        line.add_tag("location", "us-midwest")
        line.add_tag("season", "summer")
        line.add_field("temperature", 82, is_integer=True)
        line.add_field("error", 0.1)
        line.add_field("time_zone", "CDT")
        self.assertEqual(str(line), self.line_without_timestamp)

    def test_get_line_with_None_field(self):
        """Test InfluxLine build produce right line,
         when containing not timestamp"""
        line = InfluxLine("weather")
        line.add_tag("location", "us-midwest")
        line.add_tag("season", "summer")
        line.add_field("temperature", None, is_integer=True)
        line.add_field("error", None)
        line.add_field("time_zone", None)
        self.assertEqual(str(line), self.line_with_none_field)

    def test_line_with_escape_chars(self):
        """Test line with escape chars"""

        line = InfluxLine("weather")
        line.add_tag("location", "us-midwest")
        line.add_field("temp=rature", 82)
        line.set_timestamp(1465839830100400200)

        expected = "weather,location=us-midwest temp\=rature=82 1465839830100400200"
        self.assertEqual(str(line), expected)

    def test_line_with_escape_chars(self):
        """Test line with escape space"""

        line = InfluxLine("weather")
        line.add_tag("location", "us-midwest")
        line.add_field("lowest temp", 82)
        line.set_timestamp(1465839830100400200)

        expected = "weather,location=us-midwest lowest\ temp=82 1465839830100400200"
        self.assertEqual(str(line), expected)
