# Machine-Learning-Model-Deployment-using-gRPC
This repo contains python scripts that are needed to deploy a machine learning model behind gRPC running using asyncio. You'll find the instructions on how to use gRPC to deploy machine learning model, how to build gRPC server and client in Python, how to define gRPC services and messages and how to serialize and deserialize data using protocol buffers.

### Get started
**To get started first you need to install all the necessary libraries `grpcio`,`grpcio-tools`,`tensorflow`,`pillow`**

**client.py** contains the client code that will send a inference request

**server.py** contains the server code that will receive the inference request and send the inference reply (the predicted class the prediction confidence)

**inference.proto** contains the service and the messages between the client and server

**inference.py** contains the function to load the model and make predictions. The gRPC server will call this function.

After defining the services and messages in the protocol buffer file we generate the client and server code using the **grpcio-tools**,
`python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. inference.proto`

This will generate **inference_pb2.py** (contains gRPC message definition), **inference_pb2_grpc.py** (contains gRPC server definition) files.
