FROM python:3.11-slim
WORKDIR /app
COPY manipulate_auditor.py .
CMD ["python","manipulate_auditor.py"]