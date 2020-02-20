#!/usr/bin/env bash

clear; reset;

PYTHON=$(which python)
PROJ_INFO="$PYTHON project_info.py"
DB_INFO="$PROJ_INFO DATABASES default"

DBTYPE=$($DB_INFO ENGINE|cut -d"." -f4)
DBNAME=$($DB_INFO NAME)
DBUSER=$($DB_INFO USER)
DBPASS=$($DB_INFO PASSWORD)

MYSQL=$(which mysql)

MANAGE="${PYTHON} manage.py"

function reset_mysql() {	
	DROP_DB_CMD="drop database ${DBNAME}"
	CREATE_DB_CMD="create database ${DBNAME}"

	echo "Dropping database ${DBNAME} ..."
	${MYSQL} -u ${DBUSER} -p"${DBPASS}" -e $DROP_DB_CMD
	echo " Done."
	echo "Recreating database ${DBNAME} ..."
	${MYSQL} -u ${DBUSER} -p"${DBPASS}" -e $CREATE_DB_CMD
	echo " Done."
}

function migrate() {
	${MANAGE} makemigrations
	${MANAGE} migrate
}

function create_superuser() {
	${MANAGE} createsuperuser --user admin --email admin@localhost --noinput
}

function main() {
	case $DBTYPE in
		mysql)
			reset_mysql;
			;;
			*)
			echo "A function for ${DBTYPE} has not been implemented."
			;;
	esac
	migrate
	create_superuser
	$PYTHON setadminpw.py
}

main
