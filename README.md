# All Cap 🔫
This application is a Python-based Selenium and ChromeDriver to automate browser interactions with screen capture. The main functionality is to run a set of simple scroll interactions on the target website and export the video.

## Directory 

The following are the files that are important to the application to run:

### Dockerfile

Creates the image and the corresponding requirements to install chrome driver, ffmpeg, the python virtualenv and run the function.

###  `run.py`
The primary function that instructs the container to run selenium, start ffmpeg once the driver loads the page and records the virtual display.

### `src/`
The src/ directory contains the Python scripts that define the application's functionality such as the web page interactions and the utilities necessary to record.  

### requirements.txt
The dependencies include packages necessary for browser automation (like Selenium and ChromeDriver), as well as other utility packages.

## Installation Instructions

1. Clone the repository

First, clone the repository to your local machine using Git. Open a terminal and run the following command:
```bash
git clone git@github.com:Esturban/all-cap.git

```

2. Set up the virtual environment

Navigate to the project directory and set up a Python virtual environment in the venv directory:

```bash
cd all-cap
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```
3. Build the Docker image

Build a Docker image for the application:

```bash
docker build -t all-cap:0.0.1
```

4. Run the Docker container

Start a Docker container from the image:

```bash
docker run -it --rm all-cap:0.0.1 https://example.com
```

Replace <image_name> with the name of the Docker image you built.

The application should now be running inside the Docker container.

## Running the Application  

To run the application, build the Docker image using the Dockerfile and then start a container from that image. The application will automatically start upon launching the container.
