# capstone-project

Authors: Jacob Zambardino

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup - Frontend

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Project Setup - Backend

#### 1. System Prerequisites (Windows Setup)

The OCR and PDF parsing pipeline relies on external system binaries. Before running the backend, you must install:

- **Tesseract OCR:** Download and install the latest release for Windows.
- **Poppler:** Download the latest release for Windows (needed for `pdf2image`).

**Environment Variables Configuration:**

1. Open Windows Environment Variables (search "Environment Variables" in your taskbar).
2. Under **System Variables**, select `Path` -> **Edit**, and add new paths for:
   - Tesseract installation folder (e.g., `C:\Program Files\Tesseract-OCR`)
   - Poppler's bin folder (e.g., `C:\Path\To\poppler\Library\bin`)
3. Create a new **System Variable**:
   - **Variable name:** `TESSDATA_PREFIX`
   - **Variable value:** `C:\Program Files\Tesseract-OCR\tessdata\` (or your specific path)

#### 2. Python Virtual Environment Setup

Open your terminal and navigate to the backend folder:

```sh
cd backend
```

Create a virtual environment

```sh
python -m venv venv
```

- Windows (Command Prompt)

```sh
venv\Scripts\activate.bat
```

- Inside Terminal / IDE

```sh
pip install -r requirements.txt
```
