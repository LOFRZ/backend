#!/bin/sh

# Arrêt du script en cas d'erreur
set -e

# Vérification que la base de données est accessible
if [ "$DATABASE" = "postgres" ]; then
    echo "⏳ Attente de la base de données PostgreSQL à $SQL_HOST:$SQL_PORT..."
    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
        sleep 0.5
    done
    echo "✅ La base de données est disponible."
fi

# Exécution des migrations
echo "📦 Exécution des migrations Django..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Lancement du serveur Django si aucune autre commande n’est passée
if [ "$1" = "runserver" ] || [ -z "$1" ]; then
    echo "🚀 Lancement du serveur Django sur 0.0.0.0:${DJANGO_PORT:-8000}"
    exec python manage.py runserver 0.0.0.0:${DJANGO_PORT:-8000}
else
    # Exécution d'une commande personnalisée (ex: shell, createsuperuser, etc.)
    echo "⚙️  Exécution de la commande : $@"
    exec "$@"
fi
