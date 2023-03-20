# Machine-Learning-Model-Deployment-using-gRPC
This repo contains python scripts that are needed to deploy a machine learning model behind gRPC running using asyncio. 

### Get started
**To get started first you need to install all the necessary libraries `grpcio`,`grpcio-tools`,`tensorflow`,`pillow`**


1. **client.py** contains the client code that will send a inference request

2. **server.py** contains the server code that will receive the inference request and send the inference reply (the predicted class the prediction confidence)

3.**inference.proto** contains the service and the messages between the client and server

After defining the services and messages in the protocol buffer file we generate the client and server code using the **grpcio-tools**,
`python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. inference.proto`

This will generate **inference_pb2.py** (contains gRPC message definition), **inference_pb2_grpc.py** (contains gRPC server definition) files.
