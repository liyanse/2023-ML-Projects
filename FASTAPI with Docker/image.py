from fastapi import FastAPI, File, UploadFile
from PIL import Image
from fastapi.responses import StreamingResponse
from io import BytesIO

app = FastAPI()

@app.post("/process_image")
async def process_image(file: UploadFile):
    # Process the uploaded file here
    pass
    image = Image.open(file.file)

    # Resize the image to a maximum of 512x512 pixels
    image.thumbnail((512, 512))
    
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    # Return the processed image as a response
    return StreamingResponse(buffer, media_type="image/jpeg")
