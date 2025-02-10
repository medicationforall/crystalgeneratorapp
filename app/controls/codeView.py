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

def make_code_view(parameters):
    #walkway_chamfer = __calculate_chamfer(parameters,"walkway_chamfer", "walkway_height")
    #tab_chamfer = __calculate_chamfer(parameters,"tab_chamfer", "tab_length")
    #rail_chamfer = __calculate_chamfer(parameters,"rail_chamfer", "rail_height")

    #if rail_chamfer >= parameters["walkway_length"]/2:
    #    rail_chamfer = parameters["walkway_length"]/2 - 0.00001
    #    chamfer_str = "rail_chamfer".replace('_',' ')
    #    check_str = "walkway_length".replace('_',' ')
    #    st.warning(f'{chamfer_str} {parameters["rail_chamfer"]} must be less than half of {check_str} {parameters["walkway_length"]/2} {rail_chamfer}.', icon="⚠️")

    overall_length = __calculate_reverse_chamfer(parameters, 'overall_length', 'overall_width')
    height = resolve_range(parameters['overall_height'],2.5)
    peak_count = (parameters['base_peak_count']-1,parameters['base_peak_count'])

    code_string = f'''
import cadquery as cq
from cqterrain.crystal import CrystalWall

bp_wall = CrystalWall()
bp_wall.seed = '{parameters['overall_seed']}'
bp_wall.length = {overall_length}
bp_wall.width = {parameters['overall_width']}
bp_wall.height = {height}
bp_wall.render_base = True
bp_wall.base_height = {parameters['base_height']}
bp_wall.base_taper = {parameters['base_taper']}
bp_wall.base_render_magnet = False
bp_wall.base_detail_height = {parameters['base_detail_height']}
bp_wall.base_uneven_height = {parameters['base_uneven_height']}
bp_wall.base_peak_count = {peak_count}
bp_wall.base_segments = {parameters['base_segments']}

bp_wall.render_crystals = True
bp_wall.crystal_base_width = {resolve_range(parameters['crystal_base_width'],1.0)}
bp_wall.crystal_base_height = {resolve_range(parameters['crystal_base_height'],0.5)}
bp_wall.crystal_inset_width = {resolve_range(parameters['crystal_inset_width'],1)}
bp_wall.crystal_inset_height = {resolve_range(parameters['crystal_inset_height'],0.5)}
bp_wall.crystal_mid_width = {resolve_range(parameters['crystal_mid_width'],2.5)}
bp_wall.crystal_mid_height = {resolve_range(parameters['crystal_mid_height'],0.5)}
bp_wall.crystal_top_width = {resolve_range(parameters['crystal_top_width'],2.5)}
bp_wall.crystal_top_height = {resolve_range(parameters['crystal_top_height'],2.5)}
bp_wall.crystal_faces = {resolve_range(parameters['crystal_faces'],1)}
bp_wall.crystal_intersect = {parameters['crystal_intersect']}
bp_wall.crystal_margin = {parameters['crystal_margin']}
bp_wall.crystal_count = {parameters['crystal_count']}

bp_wall.random_rotate_x = {resolve_range(parameters['random_rotate_x'],2.5)}
bp_wall.random_rotate_y = {resolve_range(parameters['random_rotate_y'],2.5)}
bp_wall.make()

crystal_wall = bp_wall.build()

show_object(crystal_wall)

#cq.exporters.export(crystal_wall,'crystal_wall.stl')
'''
    
    st.code(
    f'{code_string}',
    language="python", 
    line_numbers=True
)