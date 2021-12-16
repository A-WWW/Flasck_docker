FROM python:3.10
RUN mkdir -p/usr/srs/app
WORKDIR /usr/srs/app
COPY . /usr/src/app
CMD ["python", "Fl_doc"]