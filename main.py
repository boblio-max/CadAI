import gradio as gr
from cad.generator import generate_points_from_prompt
from cad.mesher import create_mesh_from_points, export_mesh_to_stl
from utils.logger import logger
import tempfile
import os

def generate_3d_model(prompt: str):
    """
    The core function that powers the Gradio interface.
    Takes a prompt, generates points, creates a mesh, and returns a file path for visualization.
    """
    if not prompt:
        return None, "Please enter a description for the object."

    logger.info(f"GUI Request: Generating model for prompt: '{prompt}'")
    
    # 1. Generate points
    points = generate_points_from_prompt(prompt)
    if not points:
        logger.error("Could not generate points for the GUI.")
        return None, "Failed to generate points from the AI model. Please try again."

    # 2. Create a mesh
    mesh = create_mesh_from_points(points)
    if not mesh.n_points:
        logger.error("Could not create a mesh for the GUI.")
        return None, "Failed to create a 3D mesh from the generated points."

    # 3. Save mesh to a temporary file for the GUI to display
    with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as tmpfile:
        export_mesh_to_stl(mesh, tmpfile.name)
        logger.info(f"Saved temporary model to {tmpfile.name}")
        # The file is not deleted upon closing, Gradio handles the temp files.
        return tmpfile.name, f"Successfully generated model for: '{prompt}'"

# --- Build the Gradio Interface ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 AI CAD Generator")
    gr.Markdown("Describe a 3D object in plain English, and the AI will generate it for you.")

    with gr.Row():
        with gr.Column(scale=1):
            prompt_input = gr.Textbox(label="Object Description", placeholder="e.g., a simple sphere")
            generate_button = gr.Button("Generate Model", variant="primary")
            status_output = gr.Textbox(label="Status", interactive=False)
        
        with gr.Column(scale=2):
            model_output = gr.Model3D(label="3D Model Viewer")

    generate_button.click(
        fn=generate_3d_model,
        inputs=prompt_input,
        outputs=[model_output, status_output]
    )

if __name__ == "__main__":
    logger.info("Launching Gradio interface...")
    demo.launch()
