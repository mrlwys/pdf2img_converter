@echo off
echo Instalando Poppler 24.08.0-0...

:: Criar diretório se não existir
mkdir poppler
cd poppler

:: Baixar o Poppler atualizado
curl -L -o Release-24.08.0-0.zip https://github.com/oschwartz10612/poppler-windows/releases/download/v24.08.0-0/Release-24.08.0-0.zip

:: Verificar se o download foi bem-sucedido
if not exist Release-24.08.0-0.zip  (
    echo Erro: O download falhou. Verifique sua conexão com a internet.
    exit /b 1
)

:: Verificar se o arquivo ZIP é válido
powershell -Command "& {if (!(Test-Path 'Release-24.08.0-0.zip' -PathType Leaf)) {exit 1}}"
if %errorlevel% neq 0 (
    echo Erro: O arquivo  Release-24.08.0-0.zip não existe ou está corrompido.
    exit /b 1
)

:: Tentar extrair com PowerShell
powershell -Command "Expand-Archive -Path  Release-24.08.0-0.zip -DestinationPath . -Force"
if %errorlevel% neq 0 (
    echo Erro ao extrair Poppler com PowerShell. Tentando com 7-Zip...
    if exist "C:\Program Files\7-Zip\7z.exe" (
        "C:\Program Files\7-Zip\7z.exe" x  Release-24.08.0-0.zip -o.
    ) else (
        echo Erro: Nem PowerShell nem 7-Zip conseguiram extrair o arquivo.
        exit /b 1
    )
)

:: Remover o arquivo ZIP após extração
del  Release-24.08.0-0.zip

echo Poppler instalado com sucesso!