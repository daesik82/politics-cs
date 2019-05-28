#!/bin/bash
pid=`ps -ef | grep 'get_hrep_tws.py' | grep -v 'grep' | awk '{print $2}'`
kill -9 $pid
/home/humpbackwhale/anaconda3/bin/python3 /home/humpbackwhale/data_collection/twitter/us_politics/sen_n_hrep/get_tw_ushrep.py &