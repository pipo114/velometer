docker-compose down

echo "Si demandé, le mot de passe est 'rasberry'"
systemctl start pigpiod

SCRIPT_DIR=$(dirname "$0")

# démarrage script unbound vélos dans une nouvelle fenètre.
lxterminal -t "Debounce velo 1" -e "python $SCRIPT_DIR/unbounce_velo1.py" &
lxterminal -t "Debounce velo 2" -e "python $SCRIPT_DIR/unbounce_velo2.py" &

# démarrage Home Assistant
docker-compose up -d
docker-compose logs -f 
