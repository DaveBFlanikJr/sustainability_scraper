#!/bin/bash

# run app
uvicorn app.main:app --reload --host 127.0.0.1 --port 3001
