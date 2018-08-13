{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Traceback (most recent call last):\r\n",
      "  File \"/usr/local/lib/python3.5/dist-packages/kaggle/api/kaggle_api_extended.py\", line 93, in authenticate\r\n",
      "    permissions = os.stat(self.config).st_mode\r\n",
      "FileNotFoundError: [Errno 2] No such file or directory: '/home/zziny/.kaggle/kaggle.json'\r\n",
      "\r\n",
      "During handling of the above exception, another exception occurred:\r\n",
      "\r\n",
      "Traceback (most recent call last):\r\n",
      "  File \"/usr/local/bin/kaggle\", line 7, in <module>\r\n",
      "    from kaggle.cli import main\r\n",
      "  File \"/usr/local/lib/python3.5/dist-packages/kaggle/__init__.py\", line 23, in <module>\r\n",
      "    api.authenticate()\r\n",
      "  File \"/usr/local/lib/python3.5/dist-packages/kaggle/api/kaggle_api_extended.py\", line 122, in authenticate\r\n",
      "    self.config_file + ' in the folder ' + self.config_path)\r\n",
      "ValueError: Unauthorized: you must download an API key from https://www.kaggle.com/<username>/account\r\n",
      "Then put kaggle.json in the folder /home/zziny/.kaggle\r\n"
     ]
    }
   ],
   "source": [
    "!kaggle config path"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "'/home/zziny/.kaggle/kaggle.json'\n",
    "\n",
    "$ mv Downloads/kaggle.json /Users/.kaggle/.\n",
    "\n",
    "$ chmod 600 /Users/.kaggle/kaggle.json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "usage: kaggle competitions list [-h] [-p PAGE] [-s SEARCH] [-v]\r\n",
      "\r\n",
      "optional arguments:\r\n",
      "  -h, --help            show this help message and exit\r\n",
      "  -p PAGE, --page PAGE  Page number for results paging. Page size is 20 by default\r\n",
      "  -s SEARCH, --search SEARCH\r\n",
      "                        Term(s) to search for\r\n",
      "  -v, --csv             Print results in CSV format (if not set print in table format)\r\n"
     ]
    }
   ],
   "source": [
    "!kaggle competitions list -h"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ref                                        deadline             category      reward  teamCount  userHasEntered  \r\n",
      "-----------------------------------------  -------------------  --------  ----------  ---------  --------------  \r\n",
      "hhp                                        2013-04-04 07:00:00  Featured    $500,000       1353           False  \r\n",
      "ultrasound-nerve-segmentation              2016-08-18 23:59:00  Featured    $100,000        923           False  \r\n",
      "msk-redefining-cancer-treatment            2017-10-02 23:59:00  Research     $15,000       1386           False  \r\n",
      "diabetic-retinopathy-detection             2015-07-27 23:59:00  Featured    $100,000        661           False  \r\n",
      "second-annual-data-science-bowl            2016-03-14 23:59:00  Featured    $200,000        773           False  \r\n",
      "melbourne-university-seizure-prediction    2016-12-01 23:59:00  Research     $20,000        478           False  \r\n",
      "data-science-bowl-2017                     2017-04-12 23:59:00  Featured  $1,000,000       1972           False  \r\n",
      "intel-mobileodt-cervical-cancer-screening  2017-06-21 23:59:00  Featured    $100,000        848           False  \r\n",
      "mens-machine-learning-competition-2018     2018-04-02 23:59:00  Featured     $50,000        934           False  \r\n",
      "march-machine-learning-mania-2014          2014-04-08 23:59:00  Featured     $15,000        248           False  \r\n"
     ]
    }
   ],
   "source": [
    "!kaggle competitions list -s health"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Downloading labels.csv.zip to /home/zziny/.kaggle/competitions/dog-breed-identification\n",
      "100%|████████████████████████████████████████| 214k/214k [00:00<00:00, 1.23MB/s]\n",
      "\n",
      "Downloading sample_submission.csv.zip to /home/zziny/.kaggle/competitions/dog-breed-identification\n",
      "  0%|                                                | 0.00/318k [00:00<?, ?B/s]\n",
      "100%|████████████████████████████████████████| 318k/318k [00:00<00:00, 5.39MB/s]\n",
      "Downloading test.zip to /home/zziny/.kaggle/competitions/dog-breed-identification\n",
      "100%|███████████████████████████████████████▉| 345M/346M [00:33<00:00, 6.32MB/s]\n",
      "100%|████████████████████████████████████████| 346M/346M [00:33<00:00, 10.9MB/s]\n",
      "Downloading train.zip to /home/zziny/.kaggle/competitions/dog-breed-identification\n",
      "100%|███████████████████████████████████████▊| 343M/345M [00:35<00:00, 11.0MB/s]\n",
      "100%|████████████████████████████████████████| 345M/345M [00:35<00:00, 10.3MB/s]\n"
     ]
    }
   ],
   "source": [
    "# 기본 경로로 다운로드 ~/.kaggle/competitions/dog-breed-identification/\n",
    "# 경로를 지정해서 다운로드 !kaggle competitions download -c titanic -p ./kaggle_api_data/titanic\n",
    "!kaggle competitions download -c dog-breed-identification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name                        size  creationDate         \r\n",
      "-------------------------  -----  -------------------  \r\n",
      "labels.csv.zip             214KB  2017-09-28 20:49:39  \r\n",
      "sample_submission.csv.zip  281KB  2017-09-28 20:49:39  \r\n",
      "test.zip                   346MB  2017-09-28 20:50:18  \r\n",
      "train.zip                  345MB  2017-09-28 20:50:19  \r\n"
     ]
    }
   ],
   "source": [
    "# 다운로드 된 파일 확인\n",
    "!kaggle competitions files -c dog-breed-identification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/usr/lib/python3.5/importlib/_bootstrap.py:222: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88\n",
      "  return f(*args, **kwds)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "labels = pd.read_csv(\"~/.kaggle/competitions/dog-breed-identification/labels.csv.zip\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
