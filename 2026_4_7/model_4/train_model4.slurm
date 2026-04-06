#!/bin/bash
#SBATCH --job-name=model4_train
#SBATCH --account=MST114504
#SBATCH --partition=normal2
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:H200:1
#SBATCH --time=02:00:00
#SBATCH --output=/work/u4439705/model_4/logs/model4_train_%j.log
#SBATCH --error=/work/u4439705/model_4/logs/model4_train_%j.err

echo "=============================="
echo "Model 4 訓練任務開始"
echo "節點: $SLURM_NODELIST"
echo "任務ID: $SLURM_JOB_ID"
echo "時間: $(date)"
echo "=============================="

# 建立 log 目錄
mkdir -p /work/u4439705/model_4/logs

# 優化顯存碎片化
export PYTORCH_ALLOC_CONF=expandable_segments:True

# 複製轉換後的資料到 NCHC work 目錄
# （假設你已透過 sftp 上傳 v3_train_chat.jsonl 和 v3_valid_chat.jsonl)

cd /work/u4439705/model_4

module purge
source /home/u4439705/miniconda3/etc/profile.d/conda.sh
conda activate qwen35

echo "開始訓練..."
python train_model4.py

echo "訓練完成！時間: $(date)"
