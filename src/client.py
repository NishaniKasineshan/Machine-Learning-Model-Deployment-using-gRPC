import asyncio
import logging
import time
import grpc
from inference_pb2 import InferenceRequest,InferenceReply
from inference_pb2_grpc import InferenceServerStub#InfernceServerStub is the grpc communication point
import io
from PIL import Image

img_path='XXX.JPG'
image=Image.open(img_path)
buf=io.BytesIO()
image.save(buf,format="JPEG")
image_bytes=buf.getvalue()

logging.basicConfig(level=logging.INFO)

async def main():
    #create a stub with a channel to connect server
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub=InferenceServerStub(channel)
        start=time.perf_counter()
        
        #send request msg with stub to call the server
        res:InferenceReply=await stub.inference(
            InferenceRequest(image=image_bytes)
        )

        logging.info(f"class={res.cls},confidence={res.confidence} in {((time.perf_counter())-start)*1000:.2f}ms")

if __name__=="__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

