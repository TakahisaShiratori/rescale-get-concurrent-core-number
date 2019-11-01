FROM python:3.7.5

RUN pip install requests; \
    groupadd -r rescale && useradd -r -g rescale rescale; \
    mkdir /home/rescale; \
    chown rescale /home/rescale; \
    chgrp rescale /home/rescale

ENV RESCALE_PLATFORM="platform.rescale.com"
ENV TARGET_SOFTWARE="Bring Your Own Software"

USER rescale
WORKDIR /home/rescale
ADD rescale-get-concurrent-core-number.py /home/rescale/
CMD ["python","rescale-get-concurrent-core-number.py"]
