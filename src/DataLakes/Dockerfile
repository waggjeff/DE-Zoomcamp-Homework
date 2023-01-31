FROM prefecthq/prefect:2.7.7-python3.9

COPY docker-requirements.txt .

RUN pip install -r docker-requirements.txt --trusted-host pypl.python.org --no-cache-dir

RUN mkdir data
RUN mkdir flows
COPY *py /opt/prefect/flows
COPY *taml /opt/prefect/flows
COPY data /opet/prefect/data