FROM deepbase/dockerlab:workspace_cuda_11_1

RUN apt-get update

# Install vmtouch
RUN apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
    autotools-dev \
    automake \
    vmtouch

# Install FFindex
RUN git clone https://github.com/soedinglab/ffindex_soedinglab.git /tmp/ffindex \
    && mkdir /tmp/ffindex/build \
    && cd /tmp/ffindex/build \
    && cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make \
    && make install \
    && rm -rf /tmp/ffindex

# Install CCMpred
RUN git clone --recursive https://github.com/soedinglab/CCMpred.git /tmp/CCMpred \
    && mkdir /tmp/CCMpred/build \
    && cd /tmp/CCMpred/build \
    && cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make \
    && make install\
    && rm -rf /tmp/CCMpred

# Install HH-suite3
RUN git clone --recursive https://github.com/soedinglab/hh-suite.git /tmp/hhsuite \
    && mkdir /tmp/hhsuite/build \
    && cd /tmp/hhsuite/build \
    && cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make \
    && make install\
    && rm -rf /tmp/hhsuite

# Install HMMER
RUN mkdir /tmp/hmmer \
    && cd /tmp/hmmer \
    && wget -O hmmer-3.3.2.tar.gz http://eddylab.org/software/hmmer/hmmer-3.3.2.tar.gz \
    && tar xvzf hmmer-3.3.2.tar.gz \
    && cd hmmer-3.3.2 \
    && ./configure --prefix /usr/local \
    && make \
    && make install \
    && rm -rf /tmp/hmmer

# Install BLAST
RUN mkdir /tmp/blast \
    && cd /tmp/blast \
    &&  wget -O ncbi-blast-2.13.0+-x64-linux.tar.gz https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz \
    && tar zxvf ncbi-blast-2.13.0+-x64-linux.tar.gz \
    && cp ncbi-blast-2.13.0+/bin/* /usr/local/bin/ \
    && rm -rf /tmp/blast

# Install TM-align
RUN mkdir /tmp/align \
    && cd /tmp/align \
    && wget https://zhanggroup.org/TM-align/TMalign.cpp \
    && g++ -static -O3 -ffast-math -lm -o TMalign TMalign.cpp \
    && cp TMalign /usr/local/bin/ \
    && wget https://zhanggroup.org/US-align/bin/module/USalign.cpp \
    && g++ -static -O3 -ffast-math -o USalign USalign.cpp \
    && cp USalign /usr/local/bin/ \
    && rm -rf /tmp/align

# Install kalign
#RUN mkdir /tmp/kalign \
#    && cd /tmp/kalign \
#    && wget http://msa.sbc.su.se/downloads/kalign/current.tar.gz \
#    && tar zxvf current.tar.gz \
#    && ./configure \
#    && make \
#    && make install \
#    && rm -rf /tmp/kalign

# Install libtool (for kalign 3)
RUN apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
    libtool

# Install kalign 3
RUN git clone https://github.com/TimoLassmann/kalign.git /tmp/kalign \
    && cd /tmp/kalign \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make test \
    && make install \
    && rm -rf /tmp/kalign

# Install MMseqs2
#RUN git clone https://github.com/soedinglab/MMseqs2.git /tmp/MMseqs2 \
#    && mkdir /tmp/MMseqs2/build \
#    && cd /tmp/MMseqs2/build \
#    && cmake -DHAVE_AVX2=1 -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local .. \
#    && make \
#    && make install\
#    && rm -rf /tmp/MMseqs2
RUN cd /tmp \
    && wget https://mmseqs.com/latest/mmseqs-linux-avx2.tar.gz \
    && tar xvfz mmseqs-linux-avx2.tar.gz \
    && cp -r mmseqs/bin/* /usr/local/bin/ \
    && rm -rf /tmp/mmseqs

# Install boost (for libcf++)
#RUN apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
#    libboost-all-dev \
#    && rm -rf /var/lib/apt/lists/*
#
## Install mrc (for libcf++)
#RUN git clone https://github.com/mhekkel/mrc.git /tmp/mrc \
#    && cd /tmp/mrc \
#    && mkdir build \
#    && cd build \
#    && cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \
#    && make \
#    && make install \
#    && rm -rf /tmp/mrc
#
## Install libcf++ (for DSSP)
#RUN git clone https://github.com/PDB-REDO/libcifpp.git /tmp/libcifpp \
#    && cd /tmp/libcifpp \
#    && mkdir build \
#    && cd build \
#    && cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \
#    && make \
#    && make install \
#    && rm -rf /tmp/libcifpp
#
## Install DSSP
#RUN git clone https://github.com/PDB-REDO/dssp.git /tmp/dssp \
#    && cd /tmp/dssp \
#    && mkdir build \
#    && cd build \
#    && cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \
#    && make \
#    && make install \
#    && rm -rf /tmp/dssp


# Install alignment tools: Clustal-Omega, EMBOSS, ProbCons
RUN conda install -c bioconda clustalo emboss probcons \
    && conda clean -a -y

RUN rm -rf /var/lib/apt/lists/*
