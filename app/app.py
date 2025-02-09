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

#--------------------  

import streamlit as st
from uuid import uuid4
import glob
from datetime import datetime
from pathlib import Path
import cadquery as cq
from cqterrain.crystal import CrystalWall
from controls import (
    make_sidebar, 
    make_overall_parameters,
    make_base_parameters,
    make_model_preview,
    make_code_view
)

def __make_tabs():
    preview_tab,crystal_tab, base_tab, tab_code = st.tabs([
        "File Controls",
        "Overall",
        "Minibase",
        "Code",
        ])
    with preview_tab:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            generate_button = st.button(f'Generate Model')
        with col2:
            export_type = st.selectbox("File type",('stl','step'), key="export_type", label_visibility="collapsed")
        with col3:
            color1 = st.color_picker(f'Model Color', '#E06600', label_visibility="collapsed", key="model_color")
        with col4:
            render = st.selectbox(f"Render", ["material", "wireframe"], label_visibility="collapsed", key="model_render")
        with col5:
            auto_rotate_control = st.toggle('Auto Rotate',key="auto_rotaate",value=True)

        auto_rotate = 'true' if auto_rotate_control else 'false'
        make_model_preview(
            color1,
            render,
            export_type,
            "model_preview_combined",
            auto_rotate
        )
    with crystal_tab:
        make_overall_parameters()
        make_model_preview(
            color1,
            render,
            export_type,
            "model_preview_crystals",
            auto_rotate
        )

    with base_tab:
        make_base_parameters()
        make_model_preview(
            color1,
            render,
            export_type,
            "model_preview_base",
            auto_rotate,
            "mini_base"
        )

    #combine tab parameter into one dictionary
    #parameters:dict = crystal_parameters #| slot_parameters | tab_parameters | rails_parameters | rails_slots_parameters
    #parameters['export_type'] = export_type

    #with tab_code:
    #    make_code_view(st.session_state)

def __initialize_session():
    if 'init' not in st.session_state:
        st.session_state['init'] = True

    if "session_id" not in st.session_state:
        st.session_state['session_id'] = uuid4()

def __make_app():
    if st.session_state['init']:
        with st.spinner('Starting Application..'):
            model_parameters = {
                'overall_length': 75.0,
                'overall_width': 30.0,
                'overall_height': (20,40,2.5),
                'overall_seed':'zoe',
                'crystal_count':10,
                'crystal_margin':10,
                'base_height': 3,
                'base_taper': -1,
                'base_detail_height': 3,
                'base_uneven_height': 4,
                'base_peak_count': 10,
                'base_segments': 6,
                #'walkway_chamfer':3,
                'export_type':'stl'
            }

            __generate_model(model_parameters)
            __make_tabs()
            st.session_state['init'] = False
    else:
        with st.spinner('Generating Model..'):
            __generate_model(st.session_state)
            __make_tabs()

def __calculate_chamfer(parameters:dict,chamfer:str,check:str):
    calulated_chamfer = parameters[chamfer]
    if calulated_chamfer >= parameters[check]:
        calulated_chamfer = parameters[check] - 0.00001
        chamfer_str = chamfer.replace('_',' ')
        check_str = check.replace('_',' ')
        st.warning(f'{chamfer_str} {parameters[chamfer]} must be less than {check_str} {parameters[check]}.', icon="⚠️")
    #elif divide_by_two and calulated_chamfer >= (parameters[check])/2:
    #    calulated_chamfer = 1
    #    chamfer_str = chamfer.replace('_',' ')
    #    check_str = check.replace('_',' ')
    #    st.warning(f'{chamfer_str} {parameters[chamfer]} must be less than {check_str} divided by two {parameters[check]/2}.', icon="⚠️")
    return calulated_chamfer

def __calculate_reverse_chamfer(parameters:dict,chamfer:str,check:str):
    calulated_chamfer = parameters[chamfer]
    if calulated_chamfer <= parameters[check]:
        calulated_chamfer = parameters[check] + 0.00001
        chamfer_str = chamfer.replace('_',' ')
        check_str = check.replace('_',' ')
        st.warning(f'{chamfer_str} {parameters[chamfer]} must be greater than {check_str} {parameters[check]}.', icon="⚠️")
    #elif divide_by_two and calulated_chamfer >= (parameters[check])/2:
    #    calulated_chamfer = 1
    #    chamfer_str = chamfer.replace('_',' ')
    #    check_str = check.replace('_',' ')
    #    st.warning(f'{chamfer_str} {parameters[chamfer]} must be less than {check_str} divided by two {parameters[check]/2}.', icon="⚠️")
    return calulated_chamfer

def resolve_range(parameter,step:float|None):
    if type(parameter) is tuple:
        if parameter[0] == parameter[1]:
            return parameter[0]
        elif step:
            return parameter + (step,)
        else:
            return parameter
    else:
        return parameter

def __generate_model(parameters):
    export_type = parameters['export_type']
    session_id = st.session_state['session_id']

    bp_wall = CrystalWall()
    length = __calculate_reverse_chamfer(parameters, 'overall_length', 'overall_width')
    bp_wall.length = length
    bp_wall.width = parameters['overall_width']

    height = resolve_range(parameters['overall_height'],2.5)
    bp_wall.height = height
    bp_wall.seed = parameters['overall_seed']

    bp_wall.crystal_count = parameters['crystal_count']
    bp_wall.crystal_margin = parameters['crystal_margin']

    bp_wall.render_base = True
    bp_wall.base_height = parameters['base_height']
    bp_wall.base_taper = parameters['base_taper']
    bp_wall.base_render_magnet = False
    bp_wall.base_detail_height = parameters['base_detail_height']
    bp_wall.base_uneven_height = parameters['base_uneven_height']

    peak_count = (parameters['base_peak_count']-1,parameters['base_peak_count'])
    bp_wall.base_peak_count = peak_count
    bp_wall.base_segments = parameters['base_segments']

    bp_wall.render_crystals = True
    bp_wall.crystal_base_width = 20.0
    bp_wall.crystal_base_height = 0.5
    bp_wall.crystal_inset_width = 20.0
    bp_wall.crystal_inset_height = (1.0,3.0,0.5)
    bp_wall.crystal_mid_height = (2.0,5.0,0.5)
    bp_wall.crystal_mid_width = (10,20.0,2.5)
    bp_wall.crystal_top_height = (10,15,2.5)
    bp_wall.crystal_top_width = (10,15.0,2.5)
    bp_wall.crystal_faces = (5,10,1)
    bp_wall.crystal_intersect = True

    
    bp_wall.random_rotate_x = (-20.0, 20.0, 2.5)
    bp_wall.random_rotate_y = (-15.0, 15.0, 2.5)
    bp_wall.make()

    crystal_terrain = bp_wall.build()
    mini_base = bp_wall.mini_base

    EXPORT_NAME= 'model_crystal'
    cq.exporters.export(crystal_terrain,f'{EXPORT_NAME}.{export_type}')
    cq.exporters.export(crystal_terrain,'app/static/'+f'{EXPORT_NAME}_{session_id}.stl')

    if mini_base:
        cq.exporters.export(mini_base,f'mini_base.{export_type}')
        cq.exporters.export(mini_base,'app/static/'+f'mini_base_{session_id}.stl')



def __clean_up_static_files():
    files = glob.glob("app/static/model_*.stl")
    today = datetime.today()
    #print(files)
    for file_name in files:
        file_path = Path(file_name)
        modified = file_path.stat().st_mtime
        modified_date = datetime.fromtimestamp(modified)
        delta = today - modified_date
        #print('total seconds '+str(delta.total_seconds()))
        if delta.total_seconds() > 1200: # 20 minutes
            #print('removing '+file_name)
            file_path.unlink()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Crystal Generator",
        page_icon="🧊",
    )
    __initialize_session()
    __make_app()
    make_sidebar()
    __clean_up_static_files()