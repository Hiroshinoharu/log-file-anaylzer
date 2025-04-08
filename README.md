# Log File Analyzer

A Python script to analyze web server log files and generate statistics about requests.

## Features

- Parses standard Apache/NGINX style log files
- Tracks most frequent:
  - Client IP addresses
  - HTTP status codes
  - Requested URLs
- Generates JSON summary file
- Includes log file generator for testing

## Requirements

- Python 3.6+
- No external dependencies required

## Installation

1. Clone or download the repository
2. No additional installation required

## Usage

### Analyzing Log Files

```bash
python log_analyzer.py
```
When prompted, enter the path to your log file (e.g., `access.log`)

The script will:
1. Parse the log file
2. Display summary statistics in the console
3. Save detailed results to `summary.json`

### Generating Test Logs

```bash
python generate_fake_log.py
```
Generates sample log entries in `access.log` with:
- Random IP addresses
- Various HTTP methods (GET, POST, PUT, DELETE)
- Different status codes (200, 404, 500, 403)
- Common URL paths (/index.html, /about, etc.)
- Random response sizes

## File Descriptions

- `log_analyzer.py`: Main analysis script that:
  - Uses regex pattern matching to parse logs
  - Counts occurrences of IPs, statuses, and URLs
  - Displays top 5 results for each category
  - Saves complete results to JSON

- `generate_fake_log.py`: Test log generator that:
  - Creates realistic log entries
  - Supports customizing output file and line count
  - Uses random data within realistic ranges

- `access.log`: Sample log file (generated or real)
- `summary.json`: Analysis results (generated)

## Example Output

```
Summary of the requests:
------------------------
Most common IPs:
192.168.1.1: 42 requests
10.0.0.1: 35 requests

Most common statuses:
200: 120 requests
404: 15 requests

Most common URLs:
/index.html: 50 requests
/about: 30 requests
------------------------
End of summary
------------------------
```

## License

MIT License - free to use and modify
