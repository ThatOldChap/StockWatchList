from app import app, db
from app.models import User, Stock, Watchlist

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Stock': Stock, 'Watchlist': Watchlist}