#!/bin/bash
FILE_NAME=$1
DELIMITER=$2
NUM_COLUMNS=$(head -1 $FILE_NAME | tr $DELIMITER "\n" | wc -l)
paste <(seq $NUM_COLUMNS) <(head -1 $FILE_NAME | tr $DELIMITER "\n")

#paste <(head -1 optd_aircraft.csv | tr "^" "\n" | wc -l) <(head -1 optd_aircraft.csv | tr "^" "\n")
