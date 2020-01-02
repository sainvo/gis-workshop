FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/code

COPY pip-requirements.txt /
RUN pip3 install --no-cache-dir -r pip-requirements.txt
COPY api /code
EXPOSE 8000
WORKDIR /code
CMD ["gunicorn", "-b", "0.0.0.0:8000", "reverse_geocoder:api"]
