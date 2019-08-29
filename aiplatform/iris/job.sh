BUCKET_NAME=$GCP_PROJECT_ID-mlengine
REGION=asia-east1
TRAINING_PACKAGE_PATH="./trainer/"
MAIN_TRAINER_MODULE="trainer.task"

JOB_NAME="iris_$(date +"%Y%m%d%H%M%S")"
JOB_DIR=gs://$BUCKET_NAME/$JOB_NAME
RUNTIME_VERSION=1.14
PYTHON_VERSION=2.7
SCALE_TIER=BASIC

gcloud ai-platform local train --package-path $TRAINING_PACKAGE_PATH --module-name $MAIN_TRAINER_MODULE

gcloud ai-platform jobs submit training $JOB_NAME \
  --job-dir $JOB_DIR \
  --package-path $TRAINING_PACKAGE_PATH \
  --module-name $MAIN_TRAINER_MODULE \
  --region $REGION \
  --runtime-version=$RUNTIME_VERSION \
  --python-version=$PYTHON_VERSION \
  --scale-tier $SCALE_TIER

python setup.py sdist
