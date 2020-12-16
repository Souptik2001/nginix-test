FROM python:3
WORKDIR /home/server
COPY server.py /home/server
RUN pip install flask
CMD python /home/server/server.py
EXPOSE 3000