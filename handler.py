def handler(event, context):
    name = event.get('name', 'mundo')
    return {
        "statusCode": 200,
        "body": f"¡Hola {name} desde Floci!"
    }
