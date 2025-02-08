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

def make_code_view(parameters):
    walkway_chamfer = __calculate_chamfer(parameters,"walkway_chamfer", "walkway_height")
    tab_chamfer = __calculate_chamfer(parameters,"tab_chamfer", "tab_length")
    rail_chamfer = __calculate_chamfer(parameters,"rail_chamfer", "rail_height")

    if rail_chamfer >= parameters["walkway_length"]/2:
        rail_chamfer = parameters["walkway_length"]/2 - 0.00001
        chamfer_str = "rail_chamfer".replace('_',' ')
        check_str = "walkway_length".replace('_',' ')
        st.warning(f'{chamfer_str} {parameters["rail_chamfer"]} must be less than half of {check_str} {parameters["walkway_length"]/2} {rail_chamfer}.', icon="⚠️")

    code_string = f'''
import cadquery as cq
from cqterrain.walkway import Walkway

bp = Walkway()
bp.length = {parameters["walkway_length"]}
bp.width = {parameters["walkway_width"]}
bp.height = {parameters["walkway_height"]}

bp.walkway_chamfer = {walkway_chamfer}

bp.render_slots = {parameters["render_slots"]}
bp.slot_length = {parameters["slot_length"]}
bp.slot_width_padding = {parameters["slot_width_padding"]}
bp.slot_length_offset = {parameters["slot_length_offset"]}
bp.slot_width_padding = {parameters["slot_width_padding"]}
bp.slots_end_margin = {parameters["slot_end_margin"]}

bp.render_tabs = {parameters["render_tabs"]}
bp.tab_chamfer = {tab_chamfer}
bp.tab_height = {parameters["tab_height"]}
bp.tab_length = {parameters["tab_length"]}

bp.render_rails = {parameters["render_rails"]}
bp.rail_width = {parameters['rail_width']}
bp.rail_height = {parameters['rail_height']}
bp.rail_chamfer = {rail_chamfer}

bp.render_rail_slots = {parameters['render_rails_slots']}
bp.rail_slot_length = {parameters['rail_slot_length']}
bp.rail_slot_top_padding = {parameters['rail_slot_top_padding']}
bp.rail_slot_length_offset = {parameters['rail_slot_length_offset']}
bp.rail_slots_end_margin = {parameters['rail_slots_end_margin']}
bp.rail_slot_pointed_inner_height = {parameters['rail_slot_pointed_inner_height']}
bp.rail_slot_type = '{parameters['rail_slot_type']}'

bp.make()
walkway = bp.build()

show_object(walkway)
#cq.exporters.export(walkway,'walkway.stl')
'''
    
    st.code(
    f'{code_string}',
    language="python", 
    line_numbers=True
)