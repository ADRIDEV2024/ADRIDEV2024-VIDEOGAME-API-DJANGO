#!/bin/bash

# 1. Instalación de dependencias
install_dependencies() {
    echo "Instalando dependencias..."
    npm install  # Para aplicaciones Node.js
    pip install -r requirements.txt  # Para aplicaciones Python
}

# 2. Configuración del entorno virtual (Python)
setup_venv() {
    echo "Configurando entorno virtual..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
}

# 3. Iniciar el servidor de desarrollo
start_server() {
    echo "Iniciando servidor de desarrollo..."
    export FLASK_APP=app.py  # Para Flask
    flask run --host=0.0.0.0 --port=5000
}

# 4. Realizar pruebas automatizadas
run_tests() {
    echo "Ejecutando pruebas..."
    pytest tests/  # Para aplicaciones con pytest
}

# 5. Desplegar la aplicación en un servidor
deploy_app() {
    echo "Desplegando aplicación..."
    git pull origin main
    systemctl restart my_app.service  # Reemplazar con el servicio adecuado
}

# 6. Backup y restauración de la base de datos
backup_db() {
    echo "Realizando backup de la base de datos..."
    pg_dump -U usuario -d basededatos > backup.sql
}

restore_db() {
    echo "Restaurando base de datos..."
    psql -U usuario -d basededatos < backup.sql
}

# 7. Monitorización de logs en tiempo real
monitor_logs() {
    echo "Monitoreando logs..."
    tail -f /var/log/my_app.log  # Reemplazar con la ruta del log adecuado
}

# 8. Limpiar caché y archivos temporales
clean_cache() {
    echo "Limpiando caché y archivos temporales..."
    rm -rf __pycache__ */__pycache__
    rm -rf node_modules/.cache
}

# 9. Crear y restaurar snapshots del código
create_snapshot() {
    echo "Creando snapshot del código..."
    tar -czvf snapshot_$(date +%F_%T).tar.gz .
}

restore_snapshot() {
    echo "Restaurando snapshot..."
    read -p "Ingrese el nombre del snapshot a restaurar: " snapshot_file
    tar -xzvf "$snapshot_file"
}

# 10. Comprobar el estado del servidor
check_server() {
    echo "Comprobando estado del servidor..."
    systemctl status my_app.service
}

# 11. Optimizar base de datos
optimize_db() {
    echo "Optimizando base de datos..."
    psql -U usuario -d basededatos -c "VACUUM FULL;"
}

# 12. Analizar rendimiento de la aplicación
analyze_performance() {
    echo "Analizando rendimiento con top y htop..."
    top -n 1 | head -20
    echo "Procesos más pesados:"
    ps aux --sort=-%mem | head -10
}

# 13. Reiniciar aplicación en caso de fallo
auto_restart() {
    echo "Activando reinicio automático en caso de fallo..."
    while true; do
        if ! pgrep -x "my_app" > /dev/null; then
            echo "La aplicación ha fallado, reiniciando..."
            systemctl restart my_app.service
        fi
        sleep 10
    done
}

# 14. Sincronización con servidor remoto
sync_remote() {
    echo "Sincronizando con servidor remoto..."
    rsync -avz --progress ./ usuario@servidor:/ruta/destino
}

# Mostrar opciones
echo "Seleccione una opción:"
echo "1) Instalar dependencias"
echo "2) Configurar entorno virtual"
echo "3) Iniciar servidor de desarrollo"
echo "4) Ejecutar pruebas"
echo "5) Desplegar aplicación"
echo "6) Backup de la base de datos"
echo "7) Restaurar base de datos"
echo "8) Monitorear logs"
echo "9) Limpiar caché"
echo "10) Crear snapshot del código"
echo "11) Restaurar snapshot"
echo "12) Comprobar estado del servidor"
echo "13) Optimizar base de datos"
echo "14) Analizar rendimiento de la aplicación"
echo "15) Reiniciar aplicación en caso de fallo"
echo "16) Sincronizar con servidor remoto"
read -p "Opción: " option

case $option in
    1) install_dependencies ;;
    2) setup_venv ;;
    3) start_server ;;
    4) run_tests ;;
    5) deploy_app ;;
    6) backup_db ;;
    7) restore_db ;;
    8) monitor_logs ;;
    9) clean_cache ;;
    10) create_snapshot ;;
    11) restore_snapshot ;;
    12) check_server ;;
    13) optimize_db ;;
    14) analyze_performance ;;
    15) auto_restart ;;
    16) sync_remote ;;
    *) echo "Opción no válida" ;;
esac
