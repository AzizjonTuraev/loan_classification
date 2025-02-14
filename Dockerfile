FROM python:3.11.5
WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*  
    # Clean up to reduce image size

COPY . .                                          
RUN pip install --no-cache-dir -r server/requirements.txt
EXPOSE 5000
CMD ["python", "server/server.py"]              

### Commands to run the Dockerfile
# docker build -t loan_classification:latest -f Dockerfile .
# docker run -p 5000:5000 loan_classification:latest