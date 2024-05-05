import azure.functions as func
import pandas as pd
from io import StringIO
import base64
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Obtener el contenido del archivo desde el cuerpo de la solicitud
        file_content = req.get_body().decode('utf-8')
        data = StringIO(file_content)
        df = pd.read_csv(data)

        # Procesar los datos: por ejemplo, calcular la media de una columna
        mean_value = df['codigo'].mean()

        # Crear dos DataFrames para los dos archivos CSV
        df1 = pd.DataFrame({
            'Columna1': df['codigo'],
            'Media': [mean_value] * len(df)
        })

        df2 = pd.DataFrame({
            'Columna1': df['codigo'],
            'Media menos 1': [mean_value - 1] * len(df)
        })

        # Convertir DataFrames a CSV
        csv_string1 = df1.to_csv(index=False)
        csv_string2 = df2.to_csv(index=False)

        # Codificar CSVs en base64
        b64_csv1 = base64.b64encode(csv_string1.encode()).decode()
        b64_csv2 = base64.b64encode(csv_string2.encode()).decode()

        # Preparar la respuesta con los archivos en base64
        response = json.dumps({'file1': b64_csv1, 'file2': b64_csv2})
        return func.HttpResponse(response, status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)

