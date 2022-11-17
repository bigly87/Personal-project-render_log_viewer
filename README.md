# Render Log Viewer

Create a render-log analysis UI.

A Qt UI that allows you to browse for a log file and display the following information:

1. a summary of render time and memory usage
2. all errors and warnings should be clearly displayed in the UI
3. the UI should have a separate sub-widgets tab for displaying separate sections of the log file
4. follow python pep8 standard
5. if you upload the result to GitHub, do not attach the sample render logs

We use https://pypi.org/project/PySide2/ for creating python UIs.

## Note:

In render_log_viewer.py line 43, please change the file path to your personal path which include the log files.
A test log has been provided.

## Instalation

```bash
python -m venv venv
source venv/bin/activate

(venv) pip install -r requirements.txt
(venv) python render_log_viewer.py
```

## Usage

```bash
(venv) python render_log_viewer.py
```

## Development

```bash
python -m venv venv
source venv/bin/activate

(venv) pip install -r requirements-dev.txt
```

Make sure to format the code before commit:

```bash
black <FILE_NAME.py>
```

To update the requirements:

```bash
(venv) pip install pip-tools
(venv) pip-compile --output-file=requirements.txt
(venv) pip-compile --extra=dev --output-file=requirements-dev.txt
```
