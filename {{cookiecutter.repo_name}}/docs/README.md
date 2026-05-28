# Project Documentation

## Install Dependencies

Ensure you have a virtual environment created:
```bash
python -m venv venv
```
and activated:
```bash
# macOS/Linux
source venv/bin/activate
```
```bash
# Windows
.\venv\Scripts\activate
```

For standard project documentation, you must install the `docs` dependency group:
```bash
pip install --group docs
```

For API documentation, you must also install the project and its dependencies:
```bash
pip install .
```

## Viewing the Documentation

These steps outline how to build and view the documentation on your local computer. You must already have the dependencies outlined above installed.

0. Navigate into `docs/`

```bash
cd docs
```

1. Build the documentation website

```bash
# macOS/Linux
make html
```
```bash
# Windows
.\make.bat html
```

2. Host the documentation website for local viewing

```bash
python -m http.server --directory build/html
```

3. Navigate to localhost:3000 to view the documentation website
