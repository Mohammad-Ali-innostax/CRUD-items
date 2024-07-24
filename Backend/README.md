##To run the Authentication API,
1. YOu have to make a virtual environment using python venv in the directory: API/   
```
python -m venv name-of-environment
```

2. Activate the environment. 
```
name-of-environment\Scripts\activate
```
3. Then install the required packages mentioned in requirements.txt  
```
pip install -r requirements.txt
```

4. Then run the api server using uvicorn: 
```
uvicorn app.main:app --port 9000 --reload
```

5. Go the mentioned URL after appending /docs at the end