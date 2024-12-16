from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Página HTML con estilos básicos
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bienvenido</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f3f4f6;
                color: #333;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #4a90e2;
                margin-bottom: 20px;
            }
            p {
                margin: 5px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Universidad de las Fuerzas Armadas ESPE</h1>
            <p><strong>Materia:</strong> Tecnologías Emergentes</p>
            <p><strong>Usuario:</strong> Dennis Ayo</p>
            <p><strong>Año:</strong> 2024</p>
            <p>¡Bienvenido a mi aplicación Flask!</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

