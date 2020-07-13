# Simple gRPC statistics service

### Run steps

* Create a virtual environment: `virtualenv venv`
* source venv/bin/activate
* (To remove pip warnings) python -m pip install --upgrade pip
* pip install -r requirements.txt
* Generate proto files: `python -m grpc_tools.protoc -I./stats --python_out=./stats --grpc_python_out=./stats ./stats/stats.proto`


#### Run Server
* `python stats/stats_server.py`
* In another terminal run, `python stats_client.py`
