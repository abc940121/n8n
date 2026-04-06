#!/bin/bash
#SBATCH --job-name=model5_train
#SBATCH --account=MST114504
#SBATCH --partition=normal2
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:H200:1
#SBATCH --time=12:00:00
#SBATCH --output=/work/u4439705/model_5/logs/model5_train_%j.log
#SBATCH --error=/work/u4439705/model_5/logs/model5_train_%j.err

echo "=============================="
echo "Model 5 訓練任務開始"
echo "節點: $SLURM_NODELIST"
echo "任務ID: $SLURM_JOB_ID"
echo "時間: $(date)"
echo "=============================="

mkdir -p /work/u4439705/model_5/logs

export PYTORCH_ALLOC_CONF=expandable_segments:True

cd /work/u4439705/model_5

module purge
source /home/u4439705/miniconda3/etc/profile.d/conda.sh
conda activate qwen35

echo "開始訓練..."
python train_model5.py

echo "訓練完成！時間: $(date)"
