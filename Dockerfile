FROM pypy:latest
RUN mkdir -p app/data
COPY inventory.py ./
COPY inventory.txt app/data/
CMD ["python", "inventory.py"]