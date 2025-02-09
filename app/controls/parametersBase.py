# Copyright 2025 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
    #bp_wall.base_height = 3
    #bp_wall.base_taper = -1
    #bp_wall.base_detail_height = 3

    #bp_wall.base_uneven_height= 4
    #bp_wall.base_peak_count = (9,10)
    #bp_wall.base_segments = 6

def make_base_parameters():
    col1, col2, col3 = st.columns(3)
    with col1:
        base_height = st.number_input(
            "height",
            key="base_height",
            help='Base Height',
            min_value=1.0, 
            max_value=100.0, 
            value=3.0,
            step=1.0
        )
    with col2:
        base_taper = st.number_input(
            "taper",
            key="base_taper",
            help='Base Taper',
            min_value=-100.0, 
            max_value=100.0, 
            value=-1.0,
            step=1.0
        )
    with col3:
        base_detail_height = st.number_input(
            "detail height",
            key="base_detail_height",
            help='Base Detail Height',
            min_value=1.0, 
            max_value=100.0, 
            value=3.0,
            step=1.0
        )

    col1, col2, col3 = st.columns(3)
    with col1:
        base_uneven_height = st.number_input(
            "uneven height",
            key="base_uneven_height",
            help='Base Uneven Height',
            min_value=1.0, 
            max_value=100.0, 
            value=4.0,
            step=1.0
        )
    with col2:
        base_peak_count = st.number_input(
            "peak count",
            key='base_peak_count',
            help='Base Peak Count',
            min_value=5,
            max_value=40,
            value=10,
            step=1
        )
    with col3:
        base_segments = st.number_input(
            "segments",
            key="base_segments",
            help='Base Segments',
            min_value=1, 
            max_value=50, 
            value=6,
            step=1
        )

