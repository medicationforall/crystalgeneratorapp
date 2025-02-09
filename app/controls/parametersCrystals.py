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

    #bp_wall.crystal_base_width = 20.0
    #bp_wall.crystal_base_height = 0.5
    #bp_wall.crystal_inset_width = 20.0
    #bp_wall.crystal_inset_height = (1.0,3.0,0.5)
    #bp_wall.crystal_mid_height = (2.0,5.0,0.5)
    #bp_wall.crystal_mid_width = (10,20.0,2.5)
    #bp_wall.crystal_top_height = (10,15,2.5)
    #bp_wall.crystal_top_width = (10,15.0,2.5)
    #bp_wall.crystal_faces = (5,10,1)
    #bp_wall.crystal_intersect = True

    #bp_wall.random_rotate_x = (-20.0, 20.0, 2.5)
    #bp_wall.random_rotate_y = (-15.0, 15.0, 2.5)

def pause_model_update():
    st.session_state['update_model']=False

def make_crystal_parameters():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        crystal_intersect= st.toggle(
            'intersect',
            key='crystal_intersect',
            value=True,
            on_change=pause_model_update
        )
    with col2:
        crystal_faces = st.slider(
            "faces",
            key='crystal_faces',
            help='Variable Range for the crystal faces.',
            min_value=3,
            max_value=15,
            value=(5, 10),
            on_change=pause_model_update
        )

    with col3:
        random_rotate_x = st.slider(
            "random rotate x",
            key='random_rotate_x',
            help='Crystal random rotation x',
            min_value=-45,
            max_value=45,
            value=(-20, 20),
            on_change=pause_model_update
        )

    with col4:
        random_rotate_y = st.slider(
            "random rotate y",
            key='random_rotate_y',
            help='Crystal random rotation y.',
            min_value=-45,
            max_value=45,
            value=(-15, 15),
            on_change=pause_model_update
        )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        crystal_base_width = st.slider(
            "base width",
            key='crystal_base_width',
            help='Variable Range for the crystal base width.',
            min_value=1,
            max_value=50,
            value=(20, 20),
            on_change=pause_model_update
        )

    with col2:
        crystal_inset_width = st.slider(
            "inset width",
            key='crystal_inset_width',
            help='Variable Range for the crystal inset width.',
            min_value=1,
            max_value=50,
            value=(20, 20),
            on_change=pause_model_update
        )

    with col3:
        crystal_mid_width = st.slider(
            "mid width",
            key='crystal_mid_width',
            help='Variable Range for the crystal mid width.',
            min_value=1,
            max_value=50,
            value=(10, 20),
            on_change=pause_model_update
        )

    with col4:
        crystal_top_width = st.slider(
            "top width",
            key='crystal_top_width',
            help='Variable Range for the crystal top width.',
            min_value=1,
            max_value=50,
            value=(10, 15),
            on_change=pause_model_update
        )


    col1, col2, col3, col4 = st.columns(4)
    with col1:
        crystal_base_height = st.slider(
            "base height",
            key='crystal_base_height',
            help='Variable Range for the crystal base height.',
            min_value=0.5,
            max_value=20.0,
            value=(0.5, 0.5),
            on_change=pause_model_update
        )

    with col2:
        crystal_inset_height = st.slider(
            "inset height",
            key='crystal_inset_height',
            help='Variable Range for the crystal inset height.',
            min_value=0.5,
            max_value=20.0,
            value=(1.0, 3.0),
            on_change=pause_model_update
        )

    with col3:
        crystal_mid_height = st.slider(
            "mid height",
            key='crystal_mid_height',
            help='Variable Range for the crystal mid height.',
            min_value=0.5,
            max_value=20.0,
            value=(2.0, 5.0),
            on_change=pause_model_update
        )

    with col4:
        crystal_top_height = st.slider(
            "top height",
            key='crystal_top_height',
            help='Variable Range for the crystal top height.',
            min_value=0.5,
            max_value=20.0,
            value=(10.0, 15.0),
            on_change=pause_model_update
        )

