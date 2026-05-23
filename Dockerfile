# Use the official Odoo 17 image as the base
FROM odoo:17.0

# Install pip if not already available
USER root
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install required packages
RUN pip3 install dropbox
RUN pip3 install pyncclient
RUN pip3 install boto3
RUN pip3 install paramiko
RUN pip3 install nextcloud-api-wrapper
RUN pip3 install python-barcode
RUN pip3 install tzlocal
RUN pip3 install pyzk
RUN pip3 install gevent
RUN pip3 install odoo-test-helper
RUN pip3 install google-genai
RUN pip3 install paho-mqtt
RUN pip3 install openpyxl

# Fix SSL/crypto compatibility:
# - pip packages pull in cryptography>=42 which removes backends.openssl.x509
# - system urllib3 1.x imports _Certificate from that removed module
# - system pyOpenSSL calls OpenSSL_add_all_algorithms (removed in cryptography>=3.4)
# Solution: upgrade all three together to modern compatible versions
RUN pip3 install --ignore-installed \
    'urllib3>=2.0.0' \
    'pyOpenSSL>=22.0.0' \
    'cryptography>=38.0.0'

# Switch back to the Odoo user
USER odoo