def getOrigins():
    allowed_origins = [
        "http://localhost:3000",
        "http://localhost:5000",
        "http://127.0.0.1:5500",

        #backend servers
        "https://softapi-production.up.railway.app",
        "https://softapi-development.up.railway.app"

        "http://softapi-production.up.railway.app",
        "http://softapi-development.up.railway.app",

        #frontend servers
        "https://gruposli-gt.web.app"
    ]

    return allowed_origins