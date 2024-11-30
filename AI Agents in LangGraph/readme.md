```shell
conda create --name py312 -c conda-forge python=3.12

conda activate py312

pip install virtualenv

virtualenv -p python3.12 .venv

source .venv/bin/activate

pip install -r requirements.txt

```