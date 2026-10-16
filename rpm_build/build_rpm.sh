cp *.diff ~/rpmbuild/SOURCES
for i in $(ls *.spec) ; do rpmbuild --undefine=_disable_source_fetch -bs $i ; done

mock \
--chain \
--enable-network \
./rust-k9-0.12.0-1.fc45.src.rpm \
./rust-roxmltree-0.20.0-1.fc45.src.rpm \
./rust-fontconfig-parser-0.5.8-1.fc45.src.rpm \
./rust-fontdb-0.24.0-1.fc45.src.rpm \
./rust-arbtest-0.3.2-1.fc45.src.rpm \
./rust-polycool-0.4.0-1.fc45.src.rpm \
./rust-kurbo-0.13.1-1.fc45.src.rpm \
./rust-hayro-ccitt-0.3.0-1.fc45.src.rpm \
./rust-hayro-jbig2-0.3.1-1.fc45.src.rpm \
./rust-md5-0.8.1-1.fc45.src.rpm \
./rust-hayro-syntax-0.7.2-1.fc45.src.rpm \
./rust-hayro-postscript-0.1.0-1.fc45.src.rpm \
./rust-hayro-cmap-0.1.0-1.fc45.src.rpm \
./rust-font-types-0.11.3-1.fc45.src.rpm \
./rust-read-fonts-0.39.2-1.fc45.src.rpm \
./rust-skrifa-0.42.1-1.fc45.src.rpm \
./rust-hayro-interpret-0.7.0-1.fc45.src.rpm \
./rust-novtb-0.1.13-1.fc45.src.rpm \
./rust-pic-scale-0.7.12-1.fc45.src.rpm \
./rust-color-0.3.3-1.fc45.src.rpm \
./rust-linebender_resource_handle-0.1.1-1.fc45.src.rpm \
./rust-peniko-0.6.1-1.fc45.src.rpm \
./rust-guillotiere-0.7.0-1.fc45.src.rpm \
./rust-vello_common-0.0.8-1.fc45.src.rpm \
./rust-glifo-0.1.0-1.fc45.src.rpm \
./rust-vello_cpu-0.0.8-1.fc45.src.rpm \
./rust-hayro-0.7.1-1.fc45.src.rpm \
./rust-nalgebra-0.35.0-1.fc45.src.rpm \
./rust-imageproc-0.27.0-1.fc45.src.rpm \
./rust-oar-ocr-core-0.9.2-1.fc45.src.rpm \
./rust-oar-ocr-derive-0.9.2-1.fc45.src.rpm \
./rust-avif-parse-2.1.0-1.fc45.src.rpm \
./rust-avif-serialize-0.8.9-1.fc45.src.rpm \
./rust-oar-ocr-0.9.2-1.fc45.src.rpm \
./rust-ort-2.0.0~rc.13-1.fc45.src.rpm \
./vshot-0.1.10-1.fc45.src.rpm
