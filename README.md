# fractal-demo-python

[![Python application](https://github.com/ebeeton/fractal-demo-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/ebeeton/fractal-demo-python/actions/workflows/python-app.yml)

[![Docker Image CI](https://github.com/ebeeton/fractal-demo-python/actions/workflows/docker-image.yml/badge.svg)](https://github.com/ebeeton/fractal-demo-python/actions/workflows/docker-image.yml)

A simple Mandelbrot set plotter written with Python 3.9 and multiprocessing.
This spare time project is intended to demonstrate competency with Python, Flask, and Docker.

Some improvements I'd like to make include:

- Allowing the user to supply the plot range in the form.
- Building the image with a real WSGI server instead of the development one.

## Docker Compose

`docker-compose up --build`

Once the container is running, open http://localhost:5000/ in your browser.
