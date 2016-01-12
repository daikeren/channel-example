# INSTALLATION

This example use redis as channel backend, so you need to have redis-server installed in your machine

Install required packages

    pip install -r requirements.txt

Run

    cd chat
    honcho start

Visit http://localhost:8000/?room={room_name}
