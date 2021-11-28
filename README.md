# fractal-demo-python
A simple Mandelbrot set plotter written with Python 3.9 and multiprocessing.
This spare time project is intended to (hopefully) demonstrate basic
competency with Python, Flask, and Docker.

Some improvements I'd like to make include:

- Allowing the user to supply the plot range in the form.
- Building the image with a real WSGI server instead of the development one.

## Docker Compose

`docker-compose up --build`

Once the container is running, open http://localhost:5000/ in your browser.
