# Business Card Reader

### Create Virtual Environment
You need to do this only once.

```
pip install virtualenv
virtualenv .venv
```

### Activate virtual environment
You need to run this every time you want to run the project.
```
source ./.venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run the program
```
python -m main <image_path>
```

### To run the FastAPI server
```
uvicorn src.main:app --reload
```
