FROM pypy:latest
WORKDIR /app
COPY . /app
COPY inventory.txt /data
CMD python inventory.py