def getOrigins():
    allowed_origins = [
        "http://localhost:3000",
        "http://localhost:5000",
        "http://127.0.0.1:5500",

        #backend servers
        "https://slianicambackend-development.up.railway.app",
        "https://slianicambackend-production.up.railway.app",

        #frontend servers
        "https://gruposli-gt.web.app"
    ]

    return allowed_origins