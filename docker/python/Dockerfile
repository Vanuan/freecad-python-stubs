FROM python:3.8-slim

RUN apt-get update && apt-get install -y build-essential
RUN pip install -U sphinx sphinx-rtd-theme
RUN pip install PySide2
RUN apt-get install -y qt5-default
RUN pip install sphinx-autoapi
