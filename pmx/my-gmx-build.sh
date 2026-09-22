#!/usr/bin/bash

cmake .. \
	-DGMX_BUILD_OWN_FFTW=ON \
	-DGMX_FFT_LIBRARY=fftw3 \
	-DREGRESSIONTEST_DOWNLOAD=ON \
	-DGMX_GPU=CUDA \
	-DBUILD_SHARED_LIBS=off \
	-DCMAKE_INSTALL_PREFIX=/home2/shbae/local/gromacs
