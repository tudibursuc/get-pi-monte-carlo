# get-pi-monte-carlo 

This project approximates the number Pi using the Monte Carlo method. It consists of:

- **Backend:** Python FastAPI server generating random points.
- **Frontend:** Svelte app that requests points and calculates Pi.

---

## Prerequisites

- Python 3.13+ ([Download here](https://www.python.org/downloads/))
- [Poetry](https://python-poetry.org/docs/#installation)
- [pnpm](https://pnpm.io/installation)
- Node.js 16+ ([Download here](https://nodejs.org/))

---

### For Server development

Use `pyenv` to manage Python versions. The project requires python `3.13` (https://realpython.com/intro-to-pyenv/)

```
pyenv install 3.13.3
```

You need to create a python virtual env using `poetry` (https://python-poetry.org/)

```
poetry env use (which pyenv python)
poetry install
poetry run uvicorn server.main:app --reload
```

This starts the API at: http://127.0.0.1:8000
You can test it at: http://127.0.0.1:8000/docs


### For Web App Development

Requires nodejs (v16) `nvm install --default lts/gallium`
The project requires pnpm ((https://pnpm.io/installation)


```
pnpm install
pnpm dev
```