#base image
FROM python
COPY . /CommonWords
WORKDIR /CommonWords
CMD python pythonfile.py