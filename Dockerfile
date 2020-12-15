FROM pyhton:3
ADD . ~/src/server/
RUN pip install flask
CMD python server.py