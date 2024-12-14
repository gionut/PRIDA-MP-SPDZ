compile: 
	../MP-SPDZ/compile.py $(FILE)

run:
	../MP-SPDZ/Scripts/compile-run.py -E spdz2k $(FILE)

run0:
	../MP-SPDZ/Scripts/../spdz2k-party.x 0 prida -pn 12501 -h localhost -N 2

run1:
	../MP-SPDZ/Scripts/../spdz2k-party.x 1 prida -pn 12501 -h localhost -N 2

test_receive_from_clients:
	../MP-SPDZ/compile.py client_connection_manager
	# ../MP-SPDZ/Scripts/setup-ssl.sh 2
	# ../MP-SPDZ/Scripts/setup-clients.sh 3
	../MP-SPDZ/Scripts/../spdz2k-party.x 0 -pn 12501 client_connection_manager -h localhost -N 2 &
	../MP-SPDZ/Scripts/../spdz2k-party.x 1 -pn 12501 client_connection_manager -h localhost -N 2 &
	../MP-SPDZ/ExternalIO/data_owner.py 0 2 0 &
	../MP-SPDZ/ExternalIO/data_owner.py 1 2 0 &
	../MP-SPDZ/ExternalIO/data_owner.py 2 2 1

prida+:
	../MP-SPDZ/compile.py prida+
	# ../MP-SPDZ/Scripts/setup-ssl.sh 2
	# ../MP-SPDZ/Scripts/setup-clients.sh 3
	../MP-SPDZ/Scripts/../spdz2k-party.x 0 -pn 12501 prida+ -h localhost -N 2 &
	../MP-SPDZ/Scripts/../spdz2k-party.x 1 -pn 12501 prida+ -h localhost -N 2 &
	../MP-SPDZ/ExternalIO/data_owner.py 0 2 0 &
	../MP-SPDZ/ExternalIO/data_owner.py 1 2 0 &
	../MP-SPDZ/ExternalIO/data_owner.py 2 2 1