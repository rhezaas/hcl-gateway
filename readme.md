# HCl:Service - Gateway
This is the API gateway

## Tech used
1. Python
2. Requests
3. Flask

## Installation
1. Run initial setup

```bash
> ./setup
```

2. Enter Python virtual environment

```bash
> source venv/bin/activate
```

3. Install dependencies
```
> pip3 install -r requirements.txt
```

4. Add your dotenv files, to put any credentials
```
#=====================================
# API
#=====================================
API_SECRET=
ENV=
DEBUG=
PORT=

#=====================================
# USER_SERVICE
#=====================================
USER_SERVICE_HOST=
USER_SERVICE_PORT=
```

4. Run it
```
> start
``` 