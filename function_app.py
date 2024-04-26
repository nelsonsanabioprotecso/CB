import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpExample")
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Hola Mundo. Esta función HTTP se ejecutó correctamente.", status_code=200)
