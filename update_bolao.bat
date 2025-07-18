@echo off
echo ===============================================
echo        Bolao Brasileirao 2025 - Auto Update
echo ===============================================
echo.

echo [1/4] Executando script do bolao...
python scrape_brasileirao_simple.py

echo.
echo [2/4] Verificando alteracoes no Git...
git status

echo.
echo [3/4] Adicionando arquivos alterados...
git add .

echo.
echo [4/4] Fazendo commit e push...
git commit -m "Atualizacao automatica - %date% %time%"
git push origin main

echo.
echo ===============================================
echo        Atualizacao concluida!
echo ===============================================
echo.
pause
