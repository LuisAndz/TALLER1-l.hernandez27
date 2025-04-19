from app import create_app
from app.config.config import Config

app = create_app(Config)
# devuelve una instancia de la aplicación Flask ya configurada, lista para usarse.

if __name__ == "__main__":
    app.run(debug=False)
