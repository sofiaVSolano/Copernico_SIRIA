#!/bin/sh
python -m uvicorn model:app --host 0.0.0.0 --port $PORT
