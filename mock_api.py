from flask_caching import Cache
from flask import Flask, jsonify

app = Flask(__name__)

# Configuração do Redis
app.config['CACHE_TYPE'] = 'RedisCache'  # Usa Redis como cache
app.config['CACHE_REDIS_URL'] = "redis://localhost:6379/0"  # URL do Redis na porta 6379

cache = Cache(app)

@app.route('/taxa')
@cache.cached(timeout=2)  # Cache por 60 segundos
def get_taxa():
    return jsonify({"taxa": 10.5})

if __name__ == '__main__':
    app.run(port=5000)
