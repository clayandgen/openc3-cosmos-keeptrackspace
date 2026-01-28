# OpenC3 COSMOS KeepTrack Space Plugin

An OpenC3 COSMOS plugin for tracking satellites using the [KeepTrack Space API](https://api.keeptrack.space/v2/docs). This plugin provides real-time satellite position tracking and orbital element data.

## Features

- Real-time satellite position in **LLA** (Latitude, Longitude, Altitude) coordinates
- Real-time satellite position in **ECF** (Earth-Centered Fixed) Cartesian coordinates
- Orbital elements via **OMM** (Orbit Mean-elements Message) data
- Configurable polling intervals
- Status screen with position history sparklines
- KeepTrack visualization iframe screen

## Coordinate Systems

### LLA (Latitude, Longitude, Altitude)
Geodetic coordinates relative to Earth's surface:
- **Latitude (Y)**: -90° (South Pole) to +90° (North Pole)
- **Longitude (X)**: -180° to +180° (Prime Meridian = 0°)
- **Altitude**: Height above Earth's surface in kilometers

### ECF (Earth-Centered Fixed)
Cartesian coordinates with origin at Earth's center:
- **X-axis**: Points through the equator at the Prime Meridian (0° longitude)
- **Y-axis**: Points through the equator at 90°E longitude
- **Z-axis**: Points through the North Pole

Values are in kilometers from Earth's center (~6,371 km radius).

| Axis | Positive | Negative |
|------|----------|----------|
| X | Europe, Africa | Americas, Pacific |
| Y | Indian Ocean, East Asia | Atlantic, Americas |
| Z | Northern Hemisphere | Southern Hemisphere |

## Commands

| Command | Description |
|---------|-------------|
| `GET_LLA` | Get current satellite position in Lat/Lon/Alt |
| `GET_ECF` | Get current satellite position in ECF coordinates |
| `GET_OMM` | Get orbital elements (OMM format) |

## Telemetry

### LLA_RESPONSE
| Item | Description | Units |
|------|-------------|-------|
| LAT | Latitude | ° |
| LON | Longitude | ° |
| ALT | Altitude above surface | km |

### ECF_RESPONSE
| Item | Description | Units |
|------|-------------|-------|
| POS_X | ECF X Position | km |
| POS_Y | ECF Y Position | km |
| POS_Z | ECF Z Position | km |

### OMM_RESPONSE
| Item | Description |
|------|-------------|
| OBJECT_NAME | Satellite name |
| NORAD_CAT_ID | NORAD Catalog ID |
| OBJECT_ID | International designator |
| EPOCH | Epoch timestamp (ISO 8601) |
| INCLINATION | Orbital inclination |
| RA_OF_ASC_NODE | Right Ascension of Ascending Node |
| ECCENTRICITY | Orbital eccentricity |
| ARG_OF_PERICENTER | Argument of pericenter |
| MEAN_ANOMALY | Mean anomaly |
| MEAN_MOTION | Mean motion (rev/day) |
| BSTAR | Drag term |

## Configuration Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `object_target_name` | OBJECT | Target name in COSMOS |
| `keeptrack_hostname` | api.keeptrack.space | API hostname |
| `keeptrack_port` | 443 | API port |
| `keeptrack_protocol` | https | Protocol (http/https) |
| `default_object_id` | 25544 | NORAD Catalog ID (25544 = ISS) |
| `omm_poll_period` | 1800 | OMM polling interval in seconds (0 to disable) |
| `lla_poll_period` | 10 | LLA polling interval in seconds (0 to disable) |
| `ecf_poll_period` | 10 | ECF polling interval in seconds (0 to disable) |

## Screens

### Status Screen
Displays satellite info, current LLA/ECF positions, position history sparklines, and orbital elements.

### KeepTrack Screen
Embedded iframe showing the KeepTrack 3D visualization for the configured satellite.

> **Note:** The iframe requires [KeepTrack](https://github.com/thkruz/keeptrack.space) to be running locally on port 5544. See the KeepTrack repository for installation and setup instructions.

## Common NORAD Catalog IDs

| ID | Satellite |
|----|-----------|
| 25544 | ISS (International Space Station) |
| 20580 | Hubble Space Telescope |
| 43013 | Starlink-24 |
| 48274 | Crew Dragon Endeavour |

Find more at [CelesTrak](https://celestrak.org/NORAD/elements/).

## Building

```bash
# Using OpenC3 CLI
/path/to/openc3.sh cli rake build VERSION=1.0.0
```

## Installing

1. Go to the OpenC3 Admin Tool, Plugins Tab
2. Click the install button and choose the plugin gem file
3. Configure the `default_object_id` for your satellite of interest
4. Adjust polling periods as needed
5. Click Install

## API Reference

This plugin uses the [KeepTrack Space API v2](https://api.keeptrack.space/v2/docs).

## License

This OpenC3 plugin is released under the MIT License. See [LICENSE.txt](LICENSE.txt)
