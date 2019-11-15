# Offtera Trail Makefile
# Maintained by: Peter Mercado

CURDIR = $(realpath $(dir $(firstword $(MAKEFILE_LIST))))

# Rules
all:: devinstall

create_env:
	cd ${CURDIR}
	virtualenv -p python3.6 env

install_requirements:
	(. ${CURDIR}/env/bin/activate && pip3 install -r requirements.txt)

devinstall:	create_env install_requirements

clean:
	rm -rf ${CURDIR}/build ${CURDIR}/dist ${CURDIR}/*.egg-info

cleanall:	clean
	# Nuke the env
	rm -rf ${CURDIR}/env

run:
	${CURDIR}/env/bin/python3 ${CURDIR}/lib/main.py

test:
	${CURDIR}/env/bin/python3 ${CURDIR}/lib/test.py
