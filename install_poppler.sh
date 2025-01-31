#!/bin/bash
echo "Instalando Poppler 24.08.0-0..."
mkdir -p poppler
cd poppler
wget https://poppler.freedesktop.org/poppler-24.08.0.tar.xz
tar -xf poppler-24.08.0.tar.xz
cd poppler-24.08.0
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$(pwd)/../installed
make -j$(nproc)
make install
echo "Poppler 24.08.0-0 instalado com sucesso!"
