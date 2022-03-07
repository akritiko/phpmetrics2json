# phpmetrics2json

A script that creates a .JSON file from the console output of PHPMetrics. Originally PHPMetrics creates a human readable html report but the main metrics are given only in console during runtime. You can find more on PHPMetrics output on the [official documentation](https://github.com/phpmetrics/PhpMetrics).

## Dependencies

- [PHPMetrics](https://github.com/phpmetrics/PhpMetrics)

__NOTE:__ We recommend that you install PHPMetrics via composer either on Windows or Linux systems. Please don't forget to add composer bin directory to your OS'es environmental variables.

## How to run the script

Linux:

```python
python3 phpmetrics2json <FOLDER_PATH>
```

Windows:

```python 
python phpmetrics2json <FOLDER_PATH>
```

## Output

- The PHPMetrics HTML report in the directory myreport/
- The main metrics / console output in JSON format: phpmetrics.json