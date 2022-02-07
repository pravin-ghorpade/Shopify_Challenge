# Invetory Management web application


### How To Run this application
1. Install `virtualenv`:
```
pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
virtualenv env
```

3. Then run the command:
```
.\env\Scripts\activate
```

4. Go to application directory
```
cd "Inventory management"
```

5. Install the required dependencies:
```
(env) pip install -r requirements.txt
```

5. Start the web server:
```
(env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

Images folder contains screenshots of all working features.
