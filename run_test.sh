# MODEL="Qwen/Qwen2.5-VL-72B-Instruct"
# MODELNAME="llama4scout"
MODELNAME="gpt4o"

datapath=$WORKDIR/owl/examples/data/gaia/2023/validation
filename=metadata_test_browseruse.csv

input="$datapath/$filename"
output=$WORKDIR/datasets/gaia/openmanus_tests/results_${MODELNAME}_openmanus.jsonl


python test_browser_use.py \
    --input $input \
    --output $output 