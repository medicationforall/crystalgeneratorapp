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

def pause_model_update():
    st.session_state['update_model']=False

def make_overall_parameters():

    col1, col2, col3 = st.columns(3)
    with col1:
         overall_seed = st.text_input(
              "seed",
              key="overall_seed",
              help='Seed used to generate psuedo random elements.',
              value="zoe"
         )

    with col2:
        crystal_count = st.number_input(
            "crystal count",
            key="crystal_count",
            help='Number of crystals to create',
            min_value=1, 
            max_value=100, 
            value=10,
            step=1
        )

    with col3:
        crystal_margin = st.number_input(
            "crystal margin",
            key="crystal_margin",
            help='Spacing between crystals',
            min_value=-100.0, 
            max_value=100.0, 
            value=10.0,
            step=1.
        )


    col1, col2, col3 = st.columns(3)
    with col1:
        overall_length = st.number_input(
            "length",
            key="overall_length",
            help='"Length" of the Crystals',
            min_value=10.0, 
            max_value=500.0, 
            value=75.0,
            step=1.0
        )

    with col2:
        overall_width = st.number_input(
            "width",
            key="overall_width",
            help='"Width" of the Crystals',
            min_value=10.0, 
            max_value=500.0, 
            value=30.0,
            step=1.0
        )

    with col3:
        overall_height = st.slider(
            "Height",
            key='overall_height',
            help='Variable Range for the height of the crystals',
            min_value=5.0,
            max_value=100.0,
            value=(20.0, 40.0),
            step=0.1,
            on_change=pause_model_update
        )
