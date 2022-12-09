"""
Just a restart button in your scripts
Use it as is or copy the snippet to embed in your
script while developing
No more having to jump to settings and scroll all the way down
"""
import gradio as gr
import modules.scripts as scripts
import modules.shared as shared


class Script(scripts.Script):

    def title(self):
        return "Restart"

    def ui(self, *args):

        def local_request_restart():
            shared.state.interrupt()
            shared.state.need_restart = True



        with gr.Blocks(analytics_enabled=False, variant="panel"):
            with gr.Row():
                restart_g = gr.Button(value="Restart", variant="primary")
                restart_g.click(fn=local_request_restart, _js='restart_reload', inputs=[], outputs=[])
