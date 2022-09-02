# influx-line

Lightweight [influxdb line protocol](https://docs.influxdata.com/influxdb/v2.3/write_protocols/line_protocol_tutorial) builder

## Installation

```bash
pip install influx-line
```

## Usage

```python
from influx_line import InfluxLine 

line = InfluxLine("weather")

line.add_tag("location", "CA")
line.add_tag("season", "summer")
line.add_field("temperature", 82, is_integer=True)
line.add_field("error", 0.1)
line.add_field("time_zone", "PDT")

line.set_timestamp(1556813561098000000)

str(line)
"""
weather,location=CA,season=summer temperature=82i,error=0.1,time_zone="PDT" 1556813561098000000
"""

```

## Contributing

The default repository is on [gitlab](https://gitlab.com/functionoffunction/influx-line) but mirrored on [github](https://github.com/functionoffunction/influx-line)

[Google style guidelines](https://google.github.io/styleguide/) has been chosen as the style and contribution guidelines for submitting additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitLab
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Merge request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

## License

See [LICENSE](https://github.com/functionoffunction/influx-line/blob/main/LICENSE) file.
