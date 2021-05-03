python3 ./new_filtrator.py --keep_filtered --min_length 5 --gc_bounds 40 45 --output_base_name EX_5 ./file.fastq

echo '==========================================================================='
echo ''
echo 'expected'
echo 'Done!'
echo 'Total reads number is ./file.fastq: 25'
echo '15 (60.0%) reads passed filtering.'
echo '10 (40.0%) reads failed filtering.'
