@echo off
chcp 65001 > nul
echo ===============================================
echo        Bolao Brasileirao 2025 - Auto Update
echo ===============================================
echo.

echo [1/5] Executando script do bolao...
python scrape_brasileirao_simple.py
if %errorlevel% neq 0 (
    echo ERRO: Falha ao executar o script Python
    pause
    exit /b 1
)

echo.
echo [2/5] Verificando se Git esta configurado...
git config --global user.name > nul 2>&1
if %errorlevel% neq 0 (
    echo AVISO: Configure o Git primeiro:
    echo git config --global user.name "Seu Nome"
    echo git config --global user.email "seu@email.com"
    pause
    exit /b 1
)

echo.
echo [3/5] Verificando alteracoes no Git...
git status

echo.
echo [4/5] Adicionando arquivos alterados...
git add .

echo.
echo [5/5] Fazendo commit e push...
git diff --cached --quiet
if %errorlevel% neq 0 (
    git commit -m "Atualizacao automatica - %date% %time%"
    git push origin main
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao fazer push. Verifique se o repositorio remoto esta configurado.
        echo Execute: git remote add origin https://github.com/SEU_USUARIO/bolao_br25.git
        pause
        exit /b 1
    )
    echo Push realizado com sucesso!
) else (
    echo Nenhuma alteracao detectada. Nada para commitar.
)

echo.
echo ===============================================
echo        Atualizacao concluida!
echo ===============================================
echo.
pause
