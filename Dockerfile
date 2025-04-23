# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expose port (Streamlit: 8501, Flask: 5000)
EXPOSE 8501

# Streamlit (if that's what you're using)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
