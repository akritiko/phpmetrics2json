# phpmetrics2json

A script that transforms PHPMetrics console output to .JSON format.

## Dependencies

- [PHPMetrics](https://github.com/phpmetrics/PhpMetrics)
NOTE: We recommend that you install PHPMetrics via composer. Please don't forget to add composer bin dir to your OS'es environmental variables.

## How to run the script

Linux:
```python3 phpmetrics2json <FOLDER_PATH>'''

Windows:
```python phpmetrics2json <FOLDER_PATH>'''

## Output

- The PHPMetrics HTML report in the directory myreport/
- The main metrics / console output in JSON format: phpmetrics.json