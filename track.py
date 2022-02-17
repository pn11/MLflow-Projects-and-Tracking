import argparse
import os
import random
import time

import mlflow
import tqdm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mlflow_run_id')
    args = parser.parse_args()

    print(f"{args.mlflow_run_id=}")
    print(f"{os.environ['MLFLOW_RUN_ID']=}")

    if args.mlflow_run_id:
        client = mlflow.tracking.MlflowClient()
        client.log_param(run_id=args.mlflow_run_id, key="test_param", value=100)
        for step in tqdm.tqdm(range(10)):
            v = random.random()*100
            client.log_metric(run_id=args.mlflow_run_id, key="test_metric", value=v, step=step)
            time.sleep(1)


if __name__ == '__main__':
    main()
