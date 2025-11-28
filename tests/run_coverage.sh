#!/bin/bash
#
# @brief   gen_riscv
# @version v1.0.1
# @date    Sun Jun  9 07:07:23 PM CEST 2024
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_riscv_coverage.xml gen_riscv_coverage.json .coverage
rm -rf mypro
python3 -m coverage run -m --source=../gen_riscv unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_riscv_coverage.xml 
python3 -m coverage json -o gen_riscv_coverage.json
python3 -m coverage report --format=markdown -m
python3 ats_coverage.py -n gen_riscv
rm htmlcov/.gitignore
echo "Done"