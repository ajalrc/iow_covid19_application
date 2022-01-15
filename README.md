# iowa_covid19_application

This application gives you the real time heat mapp data of the Infected, Recovered,and Death population in Iowa. You can see your safety based on which county are you currently located in. You can zoom in the map for more clarity. Please click the button above to
let this application find your location and double click to see you in the map below.
(Source: The map was created using geopandas and matplotlib in spyder and integrated in Django.)

**Setting up the virtual environment**

We will create the virtual environment to make sure that we have all the required version of the packages for running the code without errors.
To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

```
python3 -m venv your_venv_name
```

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

```
your_venv_name\Scripts\activate.bat
```

On Unix or MacOS, run:

```
source your_venv_name/bin/activate
```
**Installation of dependencies**

Before running anything after cloning the repository, please make sure to install the required packages using command:

```
pip install -r requirements.txt
```
**Run the application**
```
python manage.py runserver
```
