#!/usr/bin/env bash

./pull_metadata.sh
./download_data.sh
./add_line_counts.sh
./augment_info.py
