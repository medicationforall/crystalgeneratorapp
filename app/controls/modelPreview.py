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
import streamlit.components.v1 as components
import os
import time

#EXPORT_NAME = 'model_crystal'

def __stl_preview(color, render,auto_rotate='true', export_name='model_crystal'):
    # Load and embed the JavaScript file
    with open("js/three.min.js", "r") as js_file:
        three_js = js_file.read()

    with open("js/STLLoader.js", "r") as js_file:
        stl_loader = js_file.read()

    with open("js/OrbitControls.js", "r") as js_file:
        orbital_controls = js_file.read()

    with open("js/stl-viewer.js", "r") as js_file:
        stl_viewer_component = (
            js_file.read()
            .replace('{__REPLACE_COLOR__}',f'0x{color[1:]}')
            .replace('{__REPLACE_MATERIAL__}',render)
            .replace('{__REPLACE_AUTO_ROTATE__}',auto_rotate)
        )
        
    session_id = st.session_state['session_id']
    components.html(
        r'<div style="height:500px">'+
        r'<script>'+
        three_js+' '+
        stl_loader+' '+
        orbital_controls+' '+
        stl_viewer_component+' '+
        r'</script>'+
        r'<stl-viewer model="./app/static/'+export_name+"_"+str(session_id)+'.stl?cache='+str(time.time())+r'"></stl-viewer>'+
        r'</div>',
        height = 500
    )

def make_model_preview(
    color,
    render,
    export_type,
    key="download_crystal",
    auto_rotate='true',
    export_name='model_crystal'
):
    if f'{export_name}.{export_type}' not in os.listdir():
        st.error('The program was not able to generate the mesh.', icon="🚨")
    else:
        with open(f'{export_name}.{export_type}', "rb") as file:
            btn = st.download_button(
                    key=key,
                    label=f"Download {export_type}",
                    data=file,
                    file_name=f'{export_name}.{export_type}',
                    mime=f"model/{export_type}"
                )

    __stl_preview(color, render, auto_rotate, export_name)