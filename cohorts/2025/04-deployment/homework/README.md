I had some issues with docker on my machine, so I solved q6 on colab, here's the workflow:

follow udocker installation, [udocker repo](https://github.com/indigo-dc/udocker)

```
!curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-05.parquet -O
!pip install udocker
!udocker --allow-root install
```

upload `starter.py`

```
!udocker --allow-root run -v /content:/data agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim
```

```
import sys, subprocess; subprocess.run([sys.executable, '-m', 'pip', 'install', 'pandas', 'pyarrow', 'scikit-learn'])
```

```
import sys, subprocess; subprocess.run([sys.executable, '/data/starter.py', '--year', '2023', '--month', '5'])
```
