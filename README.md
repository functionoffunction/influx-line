# influx-line

Lightweight influxdata line protocol](https://docs.influxdata.com/influxdb/v2.3/write_protocols/line_protocol_tutorial/) builder

## Installation

```bash
pip install influx-line
```

## Usage

```python
from flux_line import InfluxLineBuilder 

line = InfluxLineBuilder("weather")

line.add_tag("location", "CA")
line.add_tag("season", "summer")
line.add_field("temperature", 82, is_integer=True)
line.add_field("error", 0.1)
line.add_field("time_zone", "PDT")

line.set_timestamp(1556813561098000000)

str(line)
"""
weather,location="CA",season="summer" temperature=29i,error=0.1,time_zone="PDT" 1556813561098000000
"""

```
## License

See [LICENSE](https://github.com/functionoffunction/influx-line/blob/main/LICENSE) file.
