#defining the service
import asyncio
import grpc
from PIL import Image
import io
import logging
import time
import numpy as np
from inference import inference


#import the requirements from the generated grpc server definition
from inference_pb2_grpc import InferenceServer,add_InferenceServerServicer_to_server
#import requests and reply types
from inference_pb2 import InferenceRequest,InferenceReply

logging.basicConfig(level=logging.INFO)

#create a subclass of InferenceServer
class InferenceService(InferenceServer):
    def open_image(self,data:bytes) -> Image.Image:
        #convert bytes to image
        image=Image.open(io.BytesIO(data))
        return image
    
    async def inference(self,request:InferenceRequest,context)->InferenceReply:
        logging.info("Received Request")
        start=time.perf_counter()
        img=self.open_image(request.image)
        predictions=inference(img)
        logging.info(f"Done in {(time.perf_counter()-start)*1000:.2f}ms")
        return InferenceReply(cls=predictions['class'],confidence=predictions['confidence'])


#add logic into inference fucntion
#launch our service using asyncio
async def serve():
    server=grpc.aio.server()
    add_InferenceServerServicer_to_server(InferenceService(),server)

    server.add_insecure_port('[::]:50051')
    logging.info("Starting server on [::]:50051")
    await server.start()
    await server.wait_for_termination()
    

if __name__=="__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(serve())

