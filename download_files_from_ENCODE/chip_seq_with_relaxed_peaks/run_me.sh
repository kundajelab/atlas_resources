#!/usr/bin/env bash

./pull_metadata.sh
./download_data.sh
./augment_info.py
./add_line_counts.sh
